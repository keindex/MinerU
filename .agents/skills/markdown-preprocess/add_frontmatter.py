# -*- coding: utf-8 -*-
"""
Markdown 后处理: 为 Markdown 文件添加 frontmatter 元数据

功能:
  1. 为指定目录下的所有 .md 文件添加 frontmatter
  2. 字段: title (取文件第一个标题) + column (书名)
  3. 已存在 frontmatter 时: 保留其他字段, 仅更新 title/column
  4. UTF-8 读写, 不改变正文

用法:
  python add_frontmatter.py \
      --dir "C:/path/to/md_folder" \
      --column "电动力学导论"

说明:
  - --column 为必填 (书名/专栏名), 可选 --auto-column 从文件第一行标题自动推断
  - title 取第一个 # ~ ###### 标题; 若无标题则用文件名
"""

import argparse
import os
import re
import glob


def find_title(text: str):
    """取文本第一个标题(# ~ ######)作为 title"""
    for line in text.split("\n"):
        m = re.match(r"^#{1,6}\s+(.+?)\s*$", line)
        if m:
            return m.group(1).strip()
    return None


def strip_frontmatter(text: str):
    """去掉开头的 --- ... --- 块, 只返回正文"""
    m = re.match(r"^---[^\n]*\n.*?\n---\s*\n?", text, re.S)
    return text[m.end():] if m else text


def build_frontmatter(title: str, column: str) -> str:
    """构造仅含 title + column 的 frontmatter 块"""
    # 去掉 title 中的引号/换行, 避免破坏 YAML
    safe_title = title.replace('"', "'").replace("\n", " ").strip()
    return (
        "---\n"
        + 'title: "%s"\n' % safe_title
        + "column: %s\n" % column
        + "---\n"
        + "\n"
    )


def process_dir(target_dir: str, column: str):
    changed, skipped = 0, 0
    for path in sorted(glob.glob(os.path.join(target_dir, "**", "*.md"), recursive=True)):
        with open(path, "r", encoding="utf-8-sig") as f:
            content = f.read()

        body = strip_frontmatter(content)
        title = find_title(body) or find_title(content) or os.path.splitext(os.path.basename(path))[0]

        new_content = build_frontmatter(title, column) + body.lstrip("\n")
        if new_content != content:
            changed += 1
            with open(path, "w", encoding="utf-8", newline="\n") as f:
                f.write(new_content)
        else:
            skipped += 1
        print("[%s] title=%r" % ("更新" if new_content != content else "跳过", title))

    print("\n共处理 %d 个文件, 更新 %d, 跳过 %d" %
          (len(glob.glob(os.path.join(target_dir, "**", "*.md"), recursive=True)), changed, skipped))


def main():
    parser = argparse.ArgumentParser(description="为 Markdown 文件添加 frontmatter (title + column)")
    parser.add_argument("--dir", required=True, help="目标目录(递归处理所有 .md)")
    parser.add_argument("--column", default="", help="书名/专栏名 (column 字段)")
    args = parser.parse_args()

    if not os.path.isdir(args.dir):
        print(f"目录不存在: {args.dir}")
        return
    if not args.column:
        print("请通过 --column 指定书名 (column 字段)")
        return

    process_dir(args.dir, args.column)


if __name__ == "__main__":
    main()