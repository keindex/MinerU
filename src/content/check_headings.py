import re
import os

files = [
    r'output\现代天体物理(上) (陆埮) (z-library.sk, 1lib.sk, z-lib.sk)_part1.pdf-9e4af331-e940-4c86-a70b-c8b09fcf77e5\full.md',
    r'output\现代天体物理(上) (陆埮) (z-library.sk, 1lib.sk, z-lib.sk)_part2.pdf-5b5bd5f0-5e48-48e2-9738-e4c12e753948\full.md',
    r'output\现代天体物理(下) (陆埮) (z-library.sk, 1lib.sk, z-lib.sk)_part1.pdf-b7f55312-dea0-44cc-ba29-b61294695473\full.md',
    r'output\现代天体物理(下) (陆埮) (z-library.sk, 1lib.sk, z-lib.sk)_part2.pdf-3778f5fd-488f-49f6-bd73-753aacdb2769\full.md',
    r'output\现代天体物理(下) (陆埮) (z-library.sk, 1lib.sk, z-lib.sk)_part3.pdf-796334e3-6530-4fac-892e-b5ce56400bff\full.md',
]
for f in files:
    with open(f, 'r', encoding='utf-8') as fh:
        text = fh.read()
    headings = re.findall(r'^(#{1,3})\s+(.+)$', text, re.MULTILINE)
    folder = os.path.basename(os.path.dirname(f))
    print(f'=== {folder[:40]}... ===')
    print(f'总标题数: {len(headings)}')
    for level, title in headings[:40]:
        prefix = '#' * len(level)
        print(f'  {prefix} {title[:70]}')
    print()
