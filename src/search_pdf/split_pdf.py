"""
将 PDF 按每 200 页拆分成多份。
"""

import os
import sys
from pypdf import PdfReader, PdfWriter


def split_pdf(input_path: str, output_dir: str, pages_per_part: int = 200):
    """
    将 PDF 按指定页数拆分成多份。
    
    Args:
        input_path: 输入 PDF 文件路径
        output_dir: 输出目录
        pages_per_part: 每份的页数（默认 200）
    """
    if not os.path.exists(input_path):
        print(f"❌ 文件不存在: {input_path}")
        return False
    
    # 创建输出目录
    os.makedirs(output_dir, exist_ok=True)
    
    # 读取 PDF
    print(f"📖 读取 PDF: {os.path.basename(input_path)}")
    try:
        reader = PdfReader(input_path)
        total_pages = len(reader.pages)
        print(f"   总页数: {total_pages}")
    except Exception as e:
        print(f"❌ 读取失败: {e}")
        return False
    
    # 计算需要拆分成多少份
    num_parts = (total_pages + pages_per_part - 1) // pages_per_part
    print(f"   将拆分成 {num_parts} 份（每份 {pages_per_part} 页）")
    
    # 获取基础文件名（不含扩展名）
    base_name = os.path.splitext(os.path.basename(input_path))[0]
    
    # 拆分
    for i in range(num_parts):
        start_page = i * pages_per_part
        end_page = min((i + 1) * pages_per_part, total_pages)
        
        # 创建新的 PDF writer
        writer = PdfWriter()
        
        # 添加页面
        for page_num in range(start_page, end_page):
            writer.add_page(reader.pages[page_num])
        
        # 生成输出文件名
        part_num = i + 1
        output_filename = f"{base_name}_part{part_num}of{num_parts}_p{start_page+1}-{end_page}.pdf"
        output_path = os.path.join(output_dir, output_filename)
        
        # 写入文件
        print(f"   📄 写入: {output_filename} (页 {start_page+1}-{end_page})")
        with open(output_path, "wb") as f:
            writer.write(f)
    
    print(f"✅ 拆分完成！共生成 {num_parts} 个文件")
    return True


def main():
    # 配置
    pdfs_dir = r"c:\Users\admin\MinerU\pdfs"
    output_base_dir = r"c:\Users\admin\MinerU\pdfs_split"
    pages_per_part = 200
    
    # 获取所有 PDF 文件
    pdf_files = [f for f in os.listdir(pdfs_dir) if f.endswith('.pdf')]
    
    if not pdf_files:
        print("❌ 没有找到 PDF 文件")
        return
    
    print(f"📂 找到 {len(pdf_files)} 个 PDF 文件")
    print(f"📁 输出目录: {output_base_dir}")
    print(f"📏 每份页数: {pages_per_part}")
    print("=" * 60)
    
    # 处理每个 PDF
    for pdf_file in sorted(pdf_files):
        input_path = os.path.join(pdfs_dir, pdf_file)
        
        # 为每个 PDF 创建子目录
        base_name = os.path.splitext(pdf_file)[0]
        output_dir = os.path.join(output_base_dir, base_name)
        
        print(f"\n{'='*60}")
        print(f"📚 处理: {pdf_file}")
        print(f"{'='*60}")
        
        split_pdf(input_path, output_dir, pages_per_part)
    
    print(f"\n{'='*60}")
    print("🎉 全部完成！")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
