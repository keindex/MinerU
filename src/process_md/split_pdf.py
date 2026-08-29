import fitz, os
input_dir = r'C:\Users\admin\MinerU\pdfs\book'
output_dir = r'C:\Users\admin\MinerU\pdfs_split'
os.makedirs(output_dir, exist_ok=True)
for f in os.listdir(input_dir):
    if f.endswith('.pdf'):
        path = os.path.join(input_dir, f)
        doc = fitz.open(path)
        total = doc.page_count
        base = os.path.splitext(f)[0]
        print(f'拆分: {f} ({total} 页)')
        for i in range(0, total, 200):
            start = i
            end = min(i+200, total)
            new_doc = fitz.open()
            new_doc.insert_pdf(doc, from_page=start, to_page=end-1)
            out_name = f'{base}_part{i//200+1}.pdf'
            out_path = os.path.join(output_dir, out_name)
            new_doc.save(out_path)
            new_doc.close()
            print(f'  -> {out_name} (第 {start+1}-{end} 页)')
        doc.close()
        os.remove(path)
        print(f'  已删除原文件: {f}')
print('完成！')