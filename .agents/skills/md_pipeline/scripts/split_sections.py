# -*- coding: utf-8 -*-
"""
通用 Markdown 章节分割器: 将长篇 Markdown 按章节层级拆分为独立文件

设计 (泛化自 markdown-section-splitter / split_ied.py):

支持的标题层级 (自动识别):
  - 章:  `## 第 X 章 章名`            (level 1)
  - 节:  `## X.Y 节名`                (level 2)
  - 小节: `## X.Y.Z 小节名`            (level 3, 归入节, 不单独建文件)
  - 罗马数字章: `## I. INTRODUCTION`   (level 1)
  - 字母节: `### A. 标题`              (level 2)

拆分级别 (用户可指定):
  - 第 1 级: 仅拆出章文件
  - 第 2 级: 章 + 节
  - 第 3 级: 章 + 节 + 小节

需要删除的内容:
  1. 前置部分: 封面/作者/出版/目录/序言 (第一个章标题之前)
  2. 附录/索引 (附录/Appendix 起至文末)
  3. 乱码/噪声标题 (如单字母 "B", "C", "D" 等索引条目)

命名规则:
  - 章文件:   {书名}.第X章.章名.md (或 {书名}.{罗马}.{标题}.md)
  - 节文件:   {书名}.第X章.章名-X.Y.节名.md
  特殊字符 (\\ / : * ? " < > |) 替换为 _, LaTeX 符号清理
"""

import re
import os
import argparse
import io
import sys

# Windows 控制台默认 GBK, 显式使用 UTF-8 输出避免中文打印乱码/报错
# (仅当未被包装时进行; 在 pipeline 中作为模块加载时 stdout 可能已包装)
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except (AttributeError, ValueError):
    pass

# 缺失的章标题 -> 章名 (从目录页人工补全; 用于标题缺失的文档)
MISSING_CHAPTER_TITLES = {
    3: "第 3 章 势",
    5: "第 5 章 静磁学",
    7: "第 7 章 电动力学",
    9: "第 9 章 电磁波",
    10: "第 10 章 势与场",
    11: "第 11 章 辐射",
}

CHAPTER_RE = re.compile(r"^##\s+(第\s*([0-9一二三四五六七八九十]+)\s*章)\s+(.+)$")
# 补充习题标题 ("第1章补充习题"), 不应被当作章标题
REVIEW_RE = re.compile(r"^##\s*第\s*[0-9一二三四五六七八九十]+\s*章\s*补充习题")
SECTION_RE = re.compile(r"^##\s+([IVXLCDM]+|\d+)\.(\d+)\s+(.+)$")
SUBSECTION_RE = re.compile(r"^##\s+([IVXLCDM]+|\d+)\.(\d+)\.(\d+)\s+(.+)$")
APPENDIX_RE = re.compile(r"^#{1,2}\s*(附录|Appendix|APPENDIX|Index|索引)\b", re.IGNORECASE)
# 特定书籍的索引/附录章节名 (仅用于正文中不出现的关键词; References 每章都有, 不能用作标志)
APPENDIX_NAME_RE = re.compile(r"^#{1,2}\s*(Key Material|Special Functions)\b", re.IGNORECASE)
LETTER_ONLY_RE = re.compile(r"^##\s+([A-Z])\s*$")
ROMAN_CHAPTER_RE = re.compile(r"^#{2,3}\s+([IVXLC]+)\.\s+(\D.+)$")
LETTER_SECTION_RE = re.compile(r"^#{3}\s+([A-Z])\.\s+(.+)$")
# 一级标题 = 章 (如 Jackson: `# Introduction to Electrostatics` + `## 1.1 Coulomb's Law`)
HASH_CHAPTER_RE = re.compile(r"^#\s+([^#].+)$")


def roman_to_int(s: str):
    """罗马数字转阿拉伯数字 (I->1, IV->4, IX->9 等)"""
    s = s.upper()
    if s.isdigit():
        return int(s)
    vals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    prev = 0
    for ch in reversed(s):
        v = vals.get(ch, 0)
        if v < prev:
            total -= v
        else:
            total += v
            prev = v
    return total


def sanitize(name: str) -> str:
    """清理文件名中的非法字符"""
    name = re.sub(r"[$^{}]", "", name)  # 先去掉 LaTeX 符号 (会引入多余下划线)
    name = re.sub(r"[\\/:*?\"<>|]", "_", name)
    name = re.sub(r"\s+", " ", name).strip()
    name = name.replace(" ", "_")        # 空格统一为下划线
    name = re.sub(r"\_+", "_", name)     # 合并多个下划线
    name = re.sub(r"[0-9]+$", "", name)  # 去掉末尾残留的上标数字 (如 $^{12}$ 的 12)
    name = name.strip("_")
    return name


def split_document(input_file, output_dir, split_level=2, book_name="", skip_frontmatter=True):
    """按章节拆分文档

    Args:
        input_file: 输入 markdown 路径
        output_dir: 输出目录
        split_level: 1/2/3 级
        book_name: 输出文件前缀 (默认取输入文件名)
        skip_frontmatter: 是否跳过 frontmatter (--- ---) 块
    """
    with open(input_file, "r", encoding="utf-8") as f:
        content = f.read()

    # 可选: 移除开头的 frontmatter 块
    if skip_frontmatter:
        content = re.sub(r"^---\n.*?\n---\s*\n?", "", content, flags=re.S)

    lines = content.split("\n")
    if not book_name:
        book_name = os.path.splitext(os.path.basename(input_file))[0]

    # 判断章节模式: 一级标题章(# 标题+数字节) 优先, 其次中文章(第X章), 再次罗马章(I.)
    has_chinese_chapters = any(CHAPTER_RE.match(l.strip()) for l in lines)
    has_roman_chapters = any(ROMAN_CHAPTER_RE.match(l.strip()) for l in lines)
    has_hash_chapters = False
    if not has_chinese_chapters:
        # 检测是否有 一级标题(#) + 数字节(## X.Y) 的组合
        hash_count = 0
        sec_count = 0
        for l in lines:
            s = l.strip()
            if HASH_CHAPTER_RE.match(s):
                hash_count += 1
            if SECTION_RE.match(s):
                sec_count += 1
        # Jackson: 封面 # 标题很多但正文 # 标题少而数字节多 -> 排除封面式小标题干扰
        has_hash_chapters = hash_count >= 2 and sec_count >= 5
        if has_hash_chapters:
            has_roman_chapters = False  # 一级标题模式优先, 禁用罗马章模式

    # ---------- 定位正文起点与附录终点 (独立扫描) ----------
    start_idx = 0
    appendix_idx = len(lines)
    # 先找附录终点 (全文扫描, 任一 附录/索引/Appendix 标题即止)
    for i, line in enumerate(lines):
        s = line.strip()
        if APPENDIX_RE.match(s) or APPENDIX_NAME_RE.match(s):
            appendix_idx = i
            break
    if has_hash_chapters:
        # 一级标题章模式: 从第一个"其后紧跟数字节(## X.Y)"的 # 标题开始作为正文起点
        # (跳过封面/序言等非正文 # 标题)
        for i in range(appendix_idx if appendix_idx < len(lines) else len(lines)):
            line = lines[i]
            s = line.strip()
            m = HASH_CHAPTER_RE.match(s)
            if not m:
                continue
            # 检查该 # 标题之后 300 行内是否出现 ## X.Y 数字节
            for j in range(i + 1, min(i + 300, len(lines))):
                if SECTION_RE.match(lines[j].strip()):
                    start_idx = i
                    break
                # 若遇到另一个 # 标题, 说明该标题后无正文, 继续找下一个
                if HASH_CHAPTER_RE.match(lines[j].strip()):
                    break
            if start_idx:
                break
    else:
        for i in range(appendix_idx if appendix_idx < len(lines) else len(lines)):
            s = lines[i].strip()
            is_ch = (CHAPTER_RE.match(s) or
                     (has_roman_chapters and ROMAN_CHAPTER_RE.match(s)))
            if start_idx == 0 and is_ch:
                start_idx = i
    if start_idx >= appendix_idx:
        start_idx = 0  # 未找到章标题时从开头处理

    body_lines = lines[start_idx:appendix_idx]

    # ---------- 扫描标题 ----------
    headers = []  # (line_idx_in_body, kind, num, title)
    # kind: 'ch' 章, 'sec' 节, 'sub' 小节(level3)
    for i, line in enumerate(body_lines):
        s = line.strip()
        if not s.startswith("#"):
            continue
        if REVIEW_RE.match(s):
            continue  # 补充习题标题, 归入章文件
        if has_chinese_chapters:
            m = CHAPTER_RE.match(s)
            if m:
                try:
                    ch_num = int(m.group(2))
                except ValueError:
                    ch_num = 0
                headers.append((i, "ch", ch_num, f"{m.group(1)} {m.group(3)}"))
                continue
            m = SECTION_RE.match(s)
            if m:
                headers.append((i, "sec", f"{int(m.group(1))}.{int(m.group(2))}",
                                (int(m.group(1)), m.group(3))))
                continue
            if split_level >= 3:
                m = SUBSECTION_RE.match(s)
                if m:
                    headers.append((i, "sub", f"{int(m.group(1))}.{int(m.group(2))}.{int(m.group(3))}",
                                    (int(m.group(1)), m.group(4))))
                    continue
        elif has_roman_chapters:
            m = ROMAN_CHAPTER_RE.match(s)
            if m:
                headers.append((i, "ch", m.group(1), f"{m.group(1)}. {m.group(2)}"))
                continue
            m = LETTER_SECTION_RE.match(s)
            if m:
                headers.append((i, "sec", m.group(1), (m.group(1), m.group(2))))
                continue
        elif has_hash_chapters:
            m = HASH_CHAPTER_RE.match(s)
            if m and m.group(1).strip():
                # 跳过封面/摘要/前言等非正文一级标题 (在第一个数字节之前的 # 不算章)
                headers.append((i, "ch", len([h for h in headers if h[1] == "ch"]) + 1, m.group(1).strip()))
                continue
            m = SECTION_RE.match(s)
            if m:
                ch_num = roman_to_int(m.group(1))
                headers.append((i, "sec", f"{m.group(1)}.{int(m.group(2))}",
                                (ch_num, m.group(3))))
                continue
            if split_level >= 3:
                m = SUBSECTION_RE.match(s)
                if m:
                    ch_num = roman_to_int(m.group(1))
                    headers.append((i, "sub", f"{m.group(1)}.{int(m.group(2))}.{int(m.group(3))}",
                                    (ch_num, m.group(4))))
                    continue
        # 其他标题忽略
        if LETTER_ONLY_RE.match(s):
            continue  # 索引单字母条目

    headers.sort(key=lambda h: h[0])

    # ---------- 构建章边界 ----------
    # 显式章标题缺失时(文档直接从 "## 3.1" 开始), 用节标题推断章边界并补全章名
    chapters = []  # (start, end, ch_num, ch_title)
    if has_chinese_chapters:
        # 收集所有显式章和所有节标题的章号, 确定每章的起止
        all_ch_nums = sorted(set(
            [h[2] for h in headers if h[1] == "ch"] + [h[3][0] for h in headers if h[1] == "sec"]
        ))
        # 每章起点: 显式章标题优先, 否则该章第一个节标题
        bound_map = {}  # ch_num -> (start_line, ch_title)
        for h in headers:
            if h[1] == "ch" and h[2] not in bound_map:
                bound_map[h[2]] = (h[0], h[3])
        for n in all_ch_nums:
            if n not in bound_map:
                first_sec = next((hh for hh in headers if hh[1] == "sec" and hh[3][0] == n), None)
                if first_sec is None:
                    continue
                bound_map[n] = (first_sec[0], MISSING_CHAPTER_TITLES.get(n, f"第 {n} 章"))
        # 按行号排序确定边界
        bounds = sorted(bound_map.items(), key=lambda kv: kv[1][0])
        for bi, (n, (start, title)) in enumerate(bounds):
            end = bounds[bi + 1][1][0] if bi + 1 < len(bounds) else len(body_lines)
            chapters.append((start, end, n, title))
    elif has_roman_chapters:
        ch_indices = [i for i, h in enumerate(headers) if h[1] == "ch"]
        for ci, hi in enumerate(ch_indices):
            start = headers[hi][0]
            end = headers[ch_indices[ci + 1]][0] if ci + 1 < len(ch_indices) else len(body_lines)
            chapters.append((start, end, headers[hi][2], headers[hi][3]))
    elif has_hash_chapters:
        # 一级标题章: 按行号顺序切分 (# 章 -> 下一个 # 章)
        ch_indices = [i for i, h in enumerate(headers) if h[1] == "ch"]
        for ci, hi in enumerate(ch_indices):
            start = headers[hi][0]
            end = headers[ch_indices[ci + 1]][0] if ci + 1 < len(ch_indices) else len(body_lines)
            chapters.append((start, end, headers[hi][2], headers[hi][3]))
    else:
        # 无章结构: 整个文件作为一个章
        chapters.append((0, len(body_lines), 1, "正文"))

    print(f"找到 {len(chapters)} 章")
    for c in chapters:
        print(f"  章 {c[2]}: {c[3]} (行 {c[0] + 1}~{c[1]})")

    # ---------- 提取节 (支持 level2/3) ----------
    sections = []  # (ch_num, ch_title, sec_num, sec_title, sub_num, sub_title, start, sub_start, end)
    if split_level >= 2:
        for ch_start, ch_end, ch_num, ch_title in chapters:
            if has_roman_chapters or has_hash_chapters:
                # 罗马/一级标题结构: 章下节按行号范围
                ch_secs = [h for h in headers if h[1] in ("sec", "sub") and ch_start <= h[0] < ch_end]
            else:
                # 中文章: 用章号匹配 (缺失章标题时按节号分组)
                ch_secs = [h for h in headers
                           if h[1] in ("sec", "sub") and h[0] >= ch_start and h[0] < ch_end]
            # 只取 sec 级别作为拆分点 (sub 归入其上一级节)
            for j, h in enumerate(ch_secs):
                if h[1] == "sub":
                    continue
                sec_end = ch_end
                for k in range(j + 1, len(ch_secs)):
                    if ch_secs[k][1] == "sec":
                        sec_end = ch_secs[k][0]
                        break
                ex = (ch_num, ch_title, h[2], h[3][1], None, None, h[0], None, sec_end)
                if split_level >= 3:
                    sub_entries = [sh for sh in ch_secs if sh[1] == "sub" and h[0] < sh[0] < sec_end]
                    for sj, sh in enumerate(sub_entries):
                        sub_end = sub_entries[sj + 1][0] if sj + 1 < len(sub_entries) else sec_end
                        sections.append((ch_num, ch_title, h[2], h[3][1], sh[2], sh[3][1], sh[0], None, sub_end))
                        # 节文件(除去小节) 范围截短
                        ex = (ch_num, ch_title, h[2], h[3][1], None, None, h[0], None, sub_entries[0][0])
                if ex and not (split_level >= 3 and sub_entries):
                    sections.append(ex)
                elif ex and split_level >= 3 and not sub_entries:
                    sections.append(ex)
        print(f"找到 {len(sections)} 个节")

    # ---------- 写出文件 ----------
    os.makedirs(output_dir, exist_ok=True)
    written = 0
    book_safe = sanitize(book_name)

    for ch_start, ch_end, ch_num, ch_title in chapters:
        # 章文件
        safe_ch = sanitize(ch_title)
        ch_fn = f"{book_safe}.{safe_ch}.md"
        with open(os.path.join(output_dir, ch_fn), "w", encoding="utf-8") as f:
            f.write("\n".join(body_lines[ch_start:ch_end]))
        written += 1
        print(f"  [章] {ch_fn} ({ch_end - ch_start} 行)")

    if split_level >= 2:
        for entry in sections:
            ch_num, ch_title, sec_num, sec_title, sub_num, sub_title, sec_start, _sec_end_v, sec_end = entry
            safe_ch = sanitize(ch_title)
            if sub_num:
                # 小节文件
                safe_sec = sanitize(sec_title)
                safe_sub = sanitize(sub_title)
                sec_fn = f"{book_safe}.{safe_ch}-{sec_num}.{safe_sec}-{sub_num}.{safe_sub}.md"
                content = "\n".join(body_lines[sec_start:sec_end])
            else:
                safe_sec = sanitize(sec_title)
                sec_fn = f"{book_safe}.{safe_ch}-{sec_num}.{safe_sec}.md"
                content = "\n".join(body_lines[sec_start:sec_end])
            with open(os.path.join(output_dir, sec_fn), "w", encoding="utf-8") as f:
                f.write(content)
            written += 1

    print(f"\n完成! 共创建 {written} 个文件于 {output_dir}")
    return written


def main():
    parser = argparse.ArgumentParser(description="按章节拆分 Markdown 文档")
    parser.add_argument("--input", required=True, help="输入 markdown 文件")
    parser.add_argument("--output-dir", required=True, help="输出目录")
    parser.add_argument("--level", type=int, default=2, help="拆分级别: 1=章, 2=章+节, 3=章+节+小节 (默认2)")
    parser.add_argument("--book", default="", help="输出文件前缀(书名), 默认取输入文件名")
    parser.add_argument("--no-skip-frontmatter", action="store_true", help="不移除开头的 frontmatter 块")
    args = parser.parse_args()

    split_document(
        args.input,
        args.output_dir,
        split_level=args.level,
        book_name=args.book,
        skip_frontmatter=not args.no_skip_frontmatter,
    )


if __name__ == "__main__":
    main()