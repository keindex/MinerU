# -*- coding: utf-8 -*-
"""为 QFTIntro 合并文件添加章节号到一级标题"""
import re

input_path = r'c:\Users\admin\MinerU\archive\QFTIntro\merged_full.md'
output_path = r'c:\Users\admin\MinerU\archive\QFTIntro\merged_full_numbered.md'

with open(input_path, 'r', encoding='utf-8') as f:
    content = f.read()

lines = content.split('\n')

# 章标题列表（按顺序）
chapter_titles = [
    "$e^{+}e^{-}$ 湮灭中的对产生",
    "Klein-Gordon场",
    "Dirac场",
    "相互作用场与费曼图",
    "量子电动力学的基本过程",
    "辐射修正：引言",
    "辐射修正：一些形式上的进展",
    "紫外截断与临界涨落",
    "泛函方法",
    "重整化与对称性",
    "重整化的系统学",
    "重整化群",
    "临界指数与标量场论",
    "强子结构的部分子模型",
    "非阿贝尔规范不变性",
    "非阿贝尔规范理论的量子化",
    "量子色动力学",
    "算符乘积与有效顶点",
    "微扰论中的反常",
    "自发对称破缺的规范理论",
]

# 将一级标题 # 标题 替换为 # 第N章 标题
chapter_idx = 0
new_lines = []
for line in lines:
    s = line.strip()
    # 匹配一级标题
    m = re.match(r'^#\s+(.+)$', s)
    if m:
        title = m.group(1).strip()
        # 检查是否匹配已知章标题
        if chapter_idx < len(chapter_titles) and title == chapter_titles[chapter_idx]:
            new_line = f"# 第 {chapter_idx + 1} 章 {title}"
            new_lines.append(new_line)
            print(f"Chapter {chapter_idx + 1}: {title}")
            chapter_idx += 1
        else:
            new_lines.append(line)
    else:
        new_lines.append(line)

print(f"\nTotal chapters numbered: {chapter_idx}")

with open(output_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(new_lines))

print(f"Written to: {output_path}")