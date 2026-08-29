import os
import re
import sys

# 添加 src/process_md 到路径
sys.path.insert(0, r'C:\Users\admin\MinerU\src\process_md')
from split_sections import sanitize

merged_path = r'C:\Users\admin\MinerU\processed\粒子物理学导论_肖振军_吕才典\粒子物理学导论.md'
sections_dir = r'C:\Users\admin\MinerU\processed\粒子物理学导论_肖振军_吕才典\sections'

with open(merged_path, 'r', encoding='utf-8') as f:
    content = f.read()

lines = content.split('\n')

# 找到 8-6 节的起始行 (行 9456)
start_idx = 9456

# 找到下一章的起始行 (第9章)
end_idx = len(lines)
for i in range(start_idx + 1, len(lines)):
    s = lines[i].strip()
    if re.match(r'^#\s+第\s*9\s*章', s) or re.match(r'^##\s+第\s*9\s*章', s):
        end_idx = i
        break

section_lines = lines[start_idx:end_idx]
print(f'内容行数: {len(section_lines)}')

# 生成文件名
sec_title = 'σ(e⁺e⁻→f⁺f⁻) 的计算*'
safe_title = sanitize(sec_title)
fn = f'8-6 {safe_title}.md'
filepath = os.path.join(sections_dir, fn)

# 添加 frontmatter
frontmatter = f'''---
title: "{sec_title}"
---

'''
full_content = frontmatter + '\n'.join(section_lines)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(full_content)

print(f'已创建: {fn} ({len(section_lines)} 行)')