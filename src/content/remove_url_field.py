#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
从指定文件夹的所有 .md 文件中删除 frontmatter 的 url 字段。

用法:
  python remove_url_field.py --dir "archive/原子核物理学"
"""

import os
import re
import argparse
from pathlib import Path


def remove_url_field(content: str) -> tuple[str, bool]:
    """
    删除 frontmatter 中的 url 字段。
    返回 (处理后的内容, 是否修改)。
    """
    # 匹配 frontmatter
    fm_match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if not fm_match:
        return content, False

    fm_text = fm_match.group(1)
    rest = content[fm_match.end():]

    # 删除 url 行（支持 url: value 或 "url": value 格式）
    new_lines = []
    modified = False
    for line in fm_text.split('\n'):
        stripped = line.strip()
        # 匹配 url: xxx 或 "url": xxx
        if re.match(r'^"?url"?\s*:\s*', stripped):
            modified = True
            continue
        new_lines.append(line)

    if not modified:
        return content, False

    new_fm = '\n'.join(new_lines)
    return f"---\n{new_fm}\n---\n{rest}", True


def process_directory(directory: str) -> None:
    """处理目录下所有 .md 文件"""
    dir_path = Path(directory)
    if not dir_path.exists():
        print(f"错误: 目录不存在: {directory}")
        return

    md_files = sorted(dir_path.glob('*.md'))
    if not md_files:
        print(f"未找到 .md 文件: {directory}")
        return

    total = len(md_files)
    modified_count = 0

    for md_file in md_files:
        try:
            content = md_file.read_text(encoding='utf-8')
        except UnicodeDecodeError:
            content = md_file.read_text(encoding='gbk', errors='ignore')

        new_content, modified = remove_url_field(content)
        if modified:
            md_file.write_text(new_content, encoding='utf-8')
            modified_count += 1
            print(f"  [已修改] {md_file.name}")
        else:
            print(f"  [跳过]   {md_file.name}")

    print(f"\n完成: 共 {total} 个文件, 修改 {modified_count} 个")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='删除 md 文件 frontmatter 中的 url 字段')
    parser.add_argument('--dir', required=True, help='目标文件夹路径')
    args = parser.parse_args()

    print(f"处理目录: {args.dir}\n")
    process_directory(args.dir)
