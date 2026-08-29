with open('process_all_books.py', 'r', encoding='utf-8') as f:
    content = f.read()
content = content.replace('dirs_str = ",".join(dirs)', 'dirs_str = "|".join(dirs)')
with open('process_all_books.py', 'w', encoding='utf-8') as f:
    f.write(content)
print('已修改')
