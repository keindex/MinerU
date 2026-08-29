#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""批量删除章节文件 frontmatter title 末尾的页码（数字）。"""
import os, re, glob

base = 'processed'
fixed = 0

for book_dir in os.listdir(base):
    sections_dir = os.path.join(base, book_dir, 'sections')
    if not os.path.isdir(sections_dir):
        continue
    for md_path in glob.glob(os.path.join(sections_dir, '*.md')):
        with open(md_path, 'r', encoding='utf-8') as f:
            content = f.read()
        # 匹配 frontmatter 中的 title 行，删除末尾的数字页码
        new_content = re.sub(
            r'^(title: ".+?)\s+\d+(")',
            r'\1\2',
            content,
            flags=re.MULTILINE
        )
        if new_content != content:
            with open(md_path, 'w', encoding='utf-8', newline='\n') as f:
                f.write(new_content)
            # 提取修改后的 title 打印
            m = re.search(r'^title: "(.+?)"', new_content, re.M)
            title_after = m.group(1) if m else '?'
            print(f'[修复] {md_path} -> title={title_after!r}')
            fixed += 1

print(f'\n共修复 {fixed} 个文件')
