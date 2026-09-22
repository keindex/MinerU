# -*- coding: utf-8 -*-
"""
将 sections/*.md frontmatter 中的 url 字段替换到 index.md 的章节链接中。

背景:
  processed/{book}/index.md 中的章节条目原本指向本地 section 文件:
    - [1.1 Preamble](sections/1.1%20Preamble.md)
  sections/1.1 Preamble.chinese.md 的 frontmatter 中记录了原始来源 url:
    url: https://zhuanlan.zhihu.com/p/2080735003407803367
  本脚本将 index.md 中的本地 sections/ 链接替换为对应的 url,
  使目录可直接跳转到原文。

匹配逻辑:
  通过解码链接路径 (去掉 sections/ 前缀和 .md 后缀) 与 section 文件名
  (去掉 .md 或 .chinese.md 后缀) 进行匹配。

用法:
  # 处理单本书:
  python src/process_md/replace_index_urls.py \
      --root processed \
      --book Introduction_to_High_Energy_Physics_Perkins

  # 处理 processed/ 下所有书籍:
  python src/process_md/replace_index_urls.py --root processed --all

  # 仅预览不写入:
  python src/process_md/replace_index_urls.py --root processed --all --dry-run
"""

import argparse
import os
import re
import sys
import urllib.parse


def extract_url_from_frontmatter(content):
    """从 markdown frontmatter 中提取 url 字段"""
    m = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not m:
        return None
    fm = m.group(1)
    url_m = re.search(r"^url:\s*(\S+)", fm, re.MULTILINE)
    if url_m:
        return url_m.group(1).strip()
    return None


def build_url_map(sections_dir):
    """建立 文件基础名 -> url 的映射"""
    url_map = {}
    if not os.path.isdir(sections_dir):
        return url_map
    for fname in os.listdir(sections_dir):
        if not fname.endswith(".md"):
            continue
        path = os.path.join(sections_dir, fname)
        with open(path, "r", encoding="utf-8") as fh:
            content = fh.read()
        url = extract_url_from_frontmatter(content)
        if not url:
            continue
        # 去掉 .md 或 .chinese.md 后缀得到基础名
        if fname.endswith(".chinese.md"):
            base = fname[: -len(".chinese.md")]
        else:
            base = fname[: -len(".md")]
        url_map[base] = url
    return url_map


# 匹配 markdown 链接 [text](sections/xxx.md)
# 使用贪婪匹配 .*, 因为文件名可能包含括号, 且一行只有一个链接
LINK_RE = re.compile(r"\[([^\]]+)\]\((sections/.*\.md)\)")


def replace_index_links(content, url_map):
    """替换内容中所有 sections/ 链接为对应 url, 返回 (新内容, 替换数)"""

    def repl(m):
        text = m.group(1)
        target = m.group(2)
        # 解码链接路径 (如 %20 -> 空格)
        rel = target[len("sections/"):]
        decoded = urllib.parse.unquote(rel)
        base = decoded[: -len(".md")] if decoded.endswith(".md") else decoded
        url = url_map.get(base)
        if url:
            return "[{}]({})".format(text, url)
        return m.group(0)

    new_content, n = LINK_RE.subn(repl, content)
    return new_content, n


def process_book(book_dir, dry_run=False):
    """处理单本书, 返回替换的链接数; 无 index.md 或无 url 时返回 None"""
    index_path = os.path.join(book_dir, "index.md")
    sections_dir = os.path.join(book_dir, "sections")
    if not os.path.isfile(index_path):
        return None

    url_map = build_url_map(sections_dir)
    if not url_map:
        print("  [跳过] sections/ 下无任何带 url frontmatter 的文件")
        return None

    with open(index_path, "r", encoding="utf-8") as fh:
        content = fh.read()

    # 检查是否还有 sections/ 链接需要替换
    if "](sections/" not in content:
        print("  [跳过] index.md 中已无 sections/ 链接")
        return None

    new_content, n = replace_index_links(content, url_map)
    if n == 0:
        print("  [跳过] 未匹配到可替换的 sections/ 链接")
        return None

    if dry_run:
        print("  [预览] 将替换 {} 个链接".format(n))
    else:
        with open(index_path, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(new_content)
        print("  [完成] 已替换 {} 个链接 -> {}".format(n, index_path))
    return n


def find_books(root):
    """找出 root 下所有含 index.md 的书籍目录"""
    books = []
    if not os.path.isdir(root):
        return books
    for name in sorted(os.listdir(root)):
        path = os.path.join(root, name)
        if os.path.isdir(path) and os.path.isfile(os.path.join(path, "index.md")):
            books.append(path)
    return books


def main():
    parser = argparse.ArgumentParser(
        description="将 sections/*.md frontmatter 中的 url 替换到 index.md 的章节链接中"
    )
    parser.add_argument("--root", default="processed", help="搜索根目录 (默认 processed/)")
    parser.add_argument("--book", default="", help="指定书名 (目录名)")
    parser.add_argument("--all", action="store_true", help="处理 root 下所有书籍")
    parser.add_argument("--dry-run", action="store_true", help="仅预览不写入")
    args = parser.parse_args()

    root = args.root
    if not os.path.isabs(root):
        root = os.path.abspath(root)

    if args.book:
        book_dir = os.path.join(root, args.book)
        if not os.path.isdir(book_dir):
            print("错误: 书籍目录不存在: {}".format(book_dir), file=sys.stderr)
            sys.exit(1)
        books = [book_dir]
    else:
        books = find_books(root)
        if not books:
            print("在 {} 下未发现含 index.md 的书籍目录".format(root))
            return

    total_replaced = 0
    for book_dir in books:
        book_name = os.path.basename(book_dir)
        print("[{}]".format(book_name))
        n = process_book(book_dir, dry_run=args.dry_run)
        if n is not None:
            total_replaced += n

    print("\n总计替换 {} 个链接".format(total_replaced))


if __name__ == "__main__":
    main()