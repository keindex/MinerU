# -*- coding: utf-8 -*-
"""Process only the Gottfried Quantum Mechanics book parts"""
import os
import shutil
import re

ROOT = r"c:\Users\yangj\dev\MinerU"
OUTPUT_DIR = os.path.join(ROOT, "processed", "Quantum Mechanics Fundamentals_Gottfried")
SECTIONS_DIR = os.path.join(OUTPUT_DIR, "sections")
IMAGES_DIR = os.path.join(SECTIONS_DIR, "images")
MERGED_NAME = "Quantum Mechanics Fundamentals.md"

folders = [
    os.path.join(ROOT, "output", "Quantum mechanics  fundamentals (Gottfried, Kurt) (z-library.sk, 1lib.sk, z-lib.sk)_part1of4_p1-200.pdf-797a0e90-66b9-40d1-8c9d-d9bc170caace"),
    os.path.join(ROOT, "output", "Quantum mechanics  fundamentals (Gottfried, Kurt) (z-library.sk, 1lib.sk, z-lib.sk)_part2of4_p201-400.pdf-7e670c23-7a0b-4cb4-825e-4dc92cad7681"),
    os.path.join(ROOT, "output", "Quantum mechanics  fundamentals (Gottfried, Kurt) (z-library.sk, 1lib.sk, z-lib.sk)_part3of4_p401-600.pdf-b37a566c-e9d4-474a-af14-e61a63a71a3e"),
    os.path.join(ROOT, "output", "Quantum mechanics  fundamentals (Gottfried, Kurt) (z-library.sk, 1lib.sk, z-lib.sk)_part4of4_p601-644.pdf-680ffb10-6303-4a6a-97e9-77de8ea1af6a"),
]

# Clean and recreate output
if os.path.exists(OUTPUT_DIR):
    shutil.rmtree(OUTPUT_DIR)
os.makedirs(IMAGES_DIR, exist_ok=True)
os.makedirs(SECTIONS_DIR, exist_ok=True)

# Step 1: Merge full.md
merged_parts = []
for i, folder in enumerate(folders):
    name = os.path.basename(folder)
    md_path = os.path.join(folder, "full.md")
    if not os.path.isfile(md_path):
        print(f"  警告: {name} 下无 full.md, 跳过")
        continue
    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()
    merged_parts.append(content)
    print(f"[{i+1}] 合并 Markdown: {name} ({len(content.splitlines())} 行)")

    # Copy images
    src_img = os.path.join(folder, "images")
    if os.path.isdir(src_img):
        for fn in sorted(os.listdir(src_img)):
            src = os.path.join(src_img, fn)
            if os.path.isfile(src):
                dst = os.path.join(IMAGES_DIR, fn)
                if not os.path.exists(dst):
                    shutil.copy2(src, dst)

merged_path = os.path.join(OUTPUT_DIR, MERGED_NAME)
with open(merged_path, "w", encoding="utf-8") as f:
    f.write("\n".join(merged_parts))
print(f"\n合并完成: {merged_path}")

# Step 2: Split sections using split_sections module
sys.path.insert(0, os.path.join(ROOT, "src", "process_md"))
import split_sections as sp

section_info = sp.split_sections(merged_path, SECTIONS_DIR, level=2, book=MERGED_NAME.replace(".md",""))
print(f"分割完成: 共 {len(section_info)} 个节文件")

# Step 3: Add frontmatter
import add_frontmatter as af
af.process_dir(SECTIONS_DIR)
print("frontmatter 添加完成")

# Step 4: Generate index
from pipeline import generate_index
generate_index(OUTPUT_DIR, SECTIONS_DIR, section_info, "Quantum Mechanics: Fundamentals")
print("index.md 生成完成")

# Cleanup merged file
os.remove(merged_path)
print("已删除合并文件")
print("\n全流程完成!")
