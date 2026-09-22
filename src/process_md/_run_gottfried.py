# -*- coding: utf-8 -*-
"""Process Gottfried Quantum Mechanics parts 1-4"""
import os
import sys
import shutil

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'src', 'process_md'))

ROOT = r'c:\Users\yangj\dev\MinerU'
OUT = os.path.join(ROOT, 'processed', 'QM_Gottfried')
SECTIONS = os.path.join(OUT, 'sections')
IMAGES = os.path.join(SECTIONS, 'images')

# Clean and recreate
if os.path.exists(OUT):
    shutil.rmtree(OUT)
os.makedirs(IMAGES, exist_ok=True)

folders = [
    os.path.join(ROOT, 'output', 'Quantum mechanics  fundamentals (Gottfried, Kurt) (z-library.sk, 1lib.sk, z-lib.sk)_part1of4_p1-200.pdf-797a0e90-66b9-40d1-8c9d-d9bc170caace'),
    os.path.join(ROOT, 'output', 'Quantum mechanics  fundamentals (Gottfried, Kurt) (z-library.sk, 1lib.sk, z-lib.sk)_part2of4_p201-400.pdf-7e670c23-7a0b-4cb4-825e-4dc92cad7681'),
    os.path.join(ROOT, 'output', 'Quantum mechanics  fundamentals (Gottfried, Kurt) (z-library.sk, 1lib.sk, z-lib.sk)_part3of4_p401-600.pdf-b37a566c-e9d4-474a-af14-e61a63a71a3e'),
    os.path.join(ROOT, 'output', 'Quantum mechanics  fundamentals (Gottfried, Kurt) (z-library.sk, 1lib.sk, z-lib.sk)_part4of4_p601-644.pdf-680ffb10-6303-4a6a-97e9-77de8ea1af6a'),
]

print('Step 1: Merging full.md files...')
parts = []
for i, f in enumerate(folders):
    name = os.path.basename(f)
    with open(os.path.join(f, 'full.md'), 'r', encoding='utf-8') as fp:
        parts.append(fp.read())
    # Copy images
    src_img = os.path.join(f, 'images')
    if os.path.isdir(src_img):
        for fn in sorted(os.listdir(src_img)):
            src = os.path.join(src_img, fn)
            dst = os.path.join(IMAGES, fn)
            if os.path.isfile(src) and not os.path.exists(dst):
                shutil.copy2(src, dst)
    print(f'  [{i+1}] {name[:60]}...')

merged = os.path.join(OUT, 'merged.md')
with open(merged, 'w', encoding='utf-8') as fp:
    fp.write('\n'.join(parts))
print(f'Merged: {merged}')

print('Step 2: Splitting sections...')
import split_sections as sp
info = sp.split_document(merged, SECTIONS, split_level=2, book_name='Quantum Mechanics Fundamentals')
print(f'Split: {len(info)} sections')

print('Step 3: Adding frontmatter...')
import add_frontmatter as af
af.process_dir(SECTIONS)
print('Frontmatter done')

print('Step 4: Generating index...')
from pipeline import generate_index
generate_index(OUT, SECTIONS, info, 'Quantum Mechanics: Fundamentals')
print('Index done')

print('Step 5: Cleaning up...')
os.remove(merged)
print('Done!')
