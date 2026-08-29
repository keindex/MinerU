#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""修复过度修剪：只删末尾数字，保留前面的空格。"""
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
        # 更精确：只匹配 title 行末尾的数字（前面可以有空格），删除数字但保留空格
        new_content = re.sub(
            r'^(title: ".+?)\s+\d+(")',
            r'\1 \2',  # 保留一个空格
            content,
            flags=re.MULTILINE
        )
        # 但如果原来没有空格（如 "一些说明"），则不需要加空格
        # 实际上更好的做法：直接删除数字，不动空格
        new_content2 = re.sub(
            r'^(title: ".+?)\s*\d+(\s*")',
            r'\1\2',
            content,
            flags=re.MULTILINE
        )
        # 重新计算：只删数字，保留原有空格状态
        # 最简单：直接替换数字部分为空
        new_content3 = re.sub(
            r'^(title: ".+?)\s+\d+(")',
            lambda m: m.group(1) + m.group(2),
            content,
            flags=re.MULTILINE
        )
        # 但上面的 lambda 仍然会删空格。正确做法：
        new_content4 = re.sub(
            r'^(title: ".+?)\s+\d+(")',
            r'\1\2',
            content,
            flags=re.MULTILINE
        )
        # 实际上我们需要的是：如果原来有空格+数字，删数字保留空格；如果没有空格直接删数字
        # 重新写：匹配数字前可选空格，删除数字和前面的可选空格中的多余部分
        # 最简单直接的方法：
        def fix_title(m):
            before = m.group(1)
            after = m.group(2)
            # 删除数字，保留 before 和 after 之间的一个空格（如果 before 末尾没有空格则加一个）
            # 但如果 before 末尾已经有空格，则保留
            if before.endswith(' '):
                return before + after
            else:
                return before + ' ' + after
        new_content5 = re.sub(
            r'^(title: ".+?)\s*\d+(")',
            fix_title,
            content,
            flags=re.MULTILINE
        )
        if new_content5 != content:
            with open(md_path, 'w', encoding='utf-8', newline='\n') as f:
                f.write(new_content5)
            m = re.search(r'^title: "(.+?)"', new_content5, re.M)
            title_after = m.group(1) if m else '?'
            print(f'[修复2] {os.path.basename(md_path)} -> title={title_after!r}')
            fixed += 1

print(f'\n共修复 {fixed} 个文件')
