with open('processed/量子力学第二卷_科恩塔诺吉/量子力学第二卷_科恩塔诺吉.md', 'r', encoding='utf-8') as f:
    content = f.read()
for i, line in enumerate(content.split('\n')):
    if line.strip().startswith('#'):
        print(i, line.strip()[:100])