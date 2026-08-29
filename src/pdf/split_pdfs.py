"""按每200页拆分PDF文件"""
import pymupdf
import os

PDFS = [
    r'C:\Users\admin\MinerU\pdfs\格里菲斯_电动力学导论_第4版_中文.pdf',
    r'C:\Users\admin\MinerU\pdfs\费恩曼物理学讲义_第1卷_新千年版.pdf',
    r'C:\Users\admin\MinerU\pdfs\费恩曼物理学讲义_第2卷_新千年版.pdf',
    r'C:\Users\admin\MinerU\pdfs\费恩曼物理学讲义_第3卷_新千年版.pdf',
]

OUTPUT_DIR = r'C:\Users\admin\MinerU\pdfs_split'
PAGES_PER_SPLIT = 200

os.makedirs(OUTPUT_DIR, exist_ok=True)

for pdf_path in PDFS:
    basename = os.path.splitext(os.path.basename(pdf_path))[0]
    doc = pymupdf.open(pdf_path)
    total = doc.page_count
    print(f"\n{'='*60}")
    print(f"处理: {basename}.pdf ({total} 页)")

    part = 1
    for start in range(0, total, PAGES_PER_SPLIT):
        end = min(start + PAGES_PER_SPLIT, total)
        out_name = f"{basename}_part{part}_p{start+1}-{end}.pdf"
        out_path = os.path.join(OUTPUT_DIR, out_name)

        new_doc = pymupdf.open()
        new_doc.insert_pdf(doc, from_page=start, to_page=end - 1)
        new_doc.save(out_path)
        new_doc.close()

        print(f"  [{part}] 第 {start+1}-{end} 页 → {out_name}")
        part += 1

    doc.close()

print(f"\n{'='*60}")
print("全部拆分完成！")
