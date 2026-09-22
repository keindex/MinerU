# -*- coding: utf-8 -*-
r"""
合并 粒子物理导论 文件夹中的小章节 (.chinese.md) 为 11 个大章节文件.

输入: BASE_DIR 下的 *.chinese.md
输出: BASE_DIR/N 第N章 标题.chinese.md

策略:
  - 按 N.M 编号识别章节归属 (N=1..11)
  - 每个 N 章按 N.M 自然升序拼接内容
  - 保留各小章节的原始 frontmatter title 仅作为该小章节标题保留在文中
  - 在每个小章节合并前去掉其 frontmatter, 仅保留正文
  - 大章节文件添加新的 frontmatter (title, column: 粒子物理)
  - 大章节文件名: "N 第N章: <中文标题>.chinese.md"

用法:
  python merge_particle_physics.py
"""

import os
import re
from pathlib import Path

BASE_DIR = Path(r"c:\Users\yangj\dev\MinerU\粒子物理导论")
COLUMN = "粒子物理"

# 大章节中文标题 (依据各章第一个小章节的标题)
CHAPTER_TITLES = {
    1:  "前言",
    2:  "经典和量子相互作用图像",
    3:  "平移和旋转算子",
    4:  "粲与美；重夸克偶素态",
    5:  "e⁺e⁻ → μ⁺μ⁻ 过程",
    6:  "颜色量子数",
    7:  "分类",
    8:  "引言",
    9:  "超对称",
    10: "哈勃定律与膨胀宇宙",
    11: "加速器",
}

# 各小章节的中文标题 (按 N.M 编号, 用于大章节内部二级标题)
# 自动从每个文件 frontmatter 提取

SECTION_RE = re.compile(r"^(\d+)\.(\d+)\s+(.+)\.chinese\.md$")
FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n(.*)", re.DOTALL)
TITLE_LINE_RE = re.compile(r"^title:\s*(.+?)\s*$", re.MULTILINE)
H2_RE = re.compile(r"^##\s+1\.1\.1\s+", re.MULTILINE)  # 仅用于检查


def extract_chapter_and_section(filename: str):
    """从文件名解析 (N, M, 原英文标题)"""
    m = SECTION_RE.match(filename)
    if not m:
        return None
    return int(m.group(1)), int(m.group(2)), m.group(3)


def parse_frontmatter(content: str):
    """分离 frontmatter 和正文, 返回 (frontmatter_dict, body)"""
    m = FRONTMATTER_RE.match(content)
    if not m:
        return {}, content
    fm_text, body = m.group(1), m.group(2)
    fm = {}
    for line in fm_text.splitlines():
        if ":" in line:
            key, val = line.split(":", 1)
            fm[key.strip()] = val.strip()
    return fm, body


def strip_leading_title_h1(body: str) -> str:
    """删除正文开头紧跟 frontmatter 的 ## 标题行(因为该标题已在原文件 frontmatter 中)"""
    lines = body.splitlines()
    out = []
    skipped = False
    for line in lines:
        if not skipped and line.strip().startswith("## "):
            skipped = True
            continue
        out.append(line)
    return "\n".join(out)


def collect_files():
    """收集所有 .chinese.md 文件, 按 (N, M) 排序"""
    files = []
    for p in BASE_DIR.glob("*.chinese.md"):
        info = extract_chapter_and_section(p.name)
        if info:
            files.append((info[0], info[1], info[2], p))
    files.sort(key=lambda x: (x[0], x[1]))
    return files


def merge_chapter(chapter_num: int, section_files, output_path: Path):
    """合并某一章的所有小章节为一个文件"""
    title = CHAPTER_TITLES.get(chapter_num, f"第{chapter_num}章")

    parts = []
    parts.append(f"---\ntitle: 第{chapter_num}章 {title}\ncolumn: {COLUMN}\n---\n\n")
    parts.append(f"# 第{chapter_num}章 {title}\n\n")

    for sec_num, sec_title_orig, fpath in section_files:
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
        fm, body = parse_frontmatter(content)
        sec_title = fm.get("title", sec_title_orig).strip()
        body = strip_leading_title_h1(body)
        body = body.lstrip("\n")
        parts.append(f"## {chapter_num}.{sec_num} {sec_title}\n\n")
        parts.append(body)
        parts.append("\n\n")

    output_path.write_text("".join(parts), encoding="utf-8")


def main():
    if not BASE_DIR.is_dir():
        print(f"错误: 目录不存在 {BASE_DIR}")
        return

    files = collect_files()
    print(f"共发现 {len(files)} 个小章节文件")

    # 按章节号分组
    chapters = {}
    for chap, sec, title_orig, p in files:
        # section_files 元素: (sec_num, sec_title_orig, fpath)
        chapters.setdefault(chap, []).append((sec, title_orig, p))

    # 输出 11 个大章节文件
    for chap in sorted(chapters.keys()):
        section_files = chapters[chap]
        # 按 N.M 排序
        section_files.sort(key=lambda x: x[0])
        out_name = f"{chap} 第{chap}章 {CHAPTER_TITLES[chap]}.chinese.md"
        out_path = BASE_DIR / out_name
        merge_chapter(chap, section_files, out_path)
        print(f"  [第{chap}章] {len(section_files)} 个小章节 -> {out_name}")

    print(f"\n完成. 共生成 {len(chapters)} 个大章节文件.")


if __name__ == "__main__":
    main()