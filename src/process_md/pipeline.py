# -*- coding: utf-8 -*-
"""
Markdown 全流程管道: 预处理(合并) → 分割 → 后处理(frontmatter) 一键完成

使用场景:
  从 output/ 读取 MinerU 导出的 PDF 识别结果 (每文件夹含 full.md + images/),
  经预处理、分割、后处理后，将整理好的 Markdown 文档放在 processed/ 文件夹中。

流程:
  步骤1 (merge): 按顺序合并各文件夹 full.md, 并合并 images/ 到 sections/images/
  步骤2 (split): 按章节层级将合并文件拆分为节文件
  步骤3 (frontmatter): 为所有拆分文件添加 title 元数据
  步骤4 (index): 生成 index.md 目录 (可点击跳转章节文件)

输出结构 (以 Jackson_经典电动力学 为例):
  processed/Jackson_经典电动力学/
      ├── index.md                  ← 目录 (可点击跳转章节文件)
      ├── Jackson_经典电动力学.md   ← 合并后的完整文档
      ├── images/                   ← 合并后的图片目录
      └── sections/                 ← 按章节拆分的独立文件 (带 frontmatter)
          ├── images/               ← 章节引用的图片
          ├── 1.1 Coulomb's_Law.md
          ├── 1.2 Electric_Field.md
          └── ...

用法示例:
  python src/process_md/pipeline.py \
      --book "Jackson_经典电动力学" \
      --out-root "processed/Jackson_经典电动力学" \
      --split-level 2

  # 或显式指定输入文件夹:
  python src/process_md/pipeline.py \
      --dirs "output/folderA,output/folderB,output/folderC" \
      --book "电动力学导论" \
      --out-root "processed/电动力学导论"
"""

import os
import sys
import argparse
import importlib.util

# 所有脚本均在同一目录下
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def load_module(name, filename):
    """从同目录加载模块"""
    path = os.path.join(SCRIPT_DIR, filename)
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def generate_index(out_root, sections_dir, section_info, book_name):
    """生成 index.md 目录文件，包含可点击跳转的章节链接"""
    if not section_info:
        print("  无章节信息，跳过 index.md 生成")
        return

    # 按章节号排序
    section_info_sorted = sorted(section_info, key=lambda x: x[0])

    # 按章分组
    chapters = {}  # ch_num -> (ch_title, [(sec_num, sec_title, filename)])
    for sec_num, sec_title, fn, ch_num, ch_title in section_info_sorted:
        if ch_num not in chapters:
            chapters[ch_num] = (ch_title, [])
        chapters[ch_num][1].append((sec_num, sec_title, fn))

    lines = []
    lines.append(f"# {book_name} — 目录\n")
    lines.append("> 点击章节标题跳转到对应文件。\n")
    lines.append("---\n")

    for ch_num in sorted(chapters.keys(), key=lambda x: (isinstance(x, int), x)):
        ch_title, secs = chapters[ch_num]
        lines.append(f"## {ch_title}\n")
        for sec_num, sec_title, fn in secs:
            # 文件名中的空格在 URL 中需要编码为 %20
            url_fn = fn.replace(" ", "%20")
            lines.append(f"- [{sec_num} {sec_title}](sections/{url_fn})")
        lines.append("")
        lines.append("---\n")

    index_content = "\n".join(lines)

    index_path = os.path.join(out_root, "index.md")
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(index_content)
    print(f"  已生成: {index_path} ({len(section_info)} 个条目)")


def parse_toc_from_markdown(content):
    """从 markdown 内容中解析目录（目录页的条目）"""
    import re
    toc_entries = []  # (ch_num, sec_num_str, sec_title)
    
    # 查找目录页区域：通常在 "## 目录" 或 "## 目 录" 之后
    lines = content.split('\n')
    in_toc = False
    for i, line in enumerate(lines):
        s = line.strip()
        # 检测目录开始
        if re.match(r'^##\s*目\s*录\s*$', s):
            in_toc = True
            continue
        # 检测目录结束（下一个一级或二级标题，非目录条目）
        if in_toc and s.startswith('#'):
            # 如果是章标题或节标题格式，可能是正文开始
            if re.match(r'^#\s+第\s*\d+\s*章', s) or re.match(r'^##\s*第\s*\d+\s*章', s):
                break
            if re.match(r'^##\s+\d+[-.]\d+', s) or re.match(r'^##\s*§\s*\d+-\d+', s):
                break
        if in_toc:
            # 解析目录条目：支持 "1-2 标题 …… 54"、"1- 3 标题 …… 54"、"§ 1-2 标题 …… 54" 等格式
            # 去掉末尾的页码部分（…… 54 或 … 54）
            m = re.match(r'^[\s\-\*\•]*\s*(?:§\s*)?(\d+)\s*[-.]\s*(\d+)\s+(.+?)(?:\s*[…·\.]{2,}\s*\d+\s*)?$', s)
            if m:
                ch_num = int(m.group(1))
                sec_num = f"{ch_num}-{int(m.group(2))}"  # 完整格式：6-1
                sec_title = m.group(3).strip()
                toc_entries.append((ch_num, sec_num, sec_title))
    return toc_entries


def find_missing_sections(merged_path, sections_dir, section_info):
    """对比目录和已生成的节文件，找出缺失的节"""
    import re
    
    # 读取合并后的完整文档
    with open(merged_path, 'r', encoding='utf-8') as f:
        merged_content = f.read()
    
    # 解析目录
    toc_entries = parse_toc_from_markdown(merged_content)
    if not toc_entries:
        print("  未检测到目录页，跳过缺失章节检查")
        return []
    
    print(f"  目录页检测到 {len(toc_entries)} 个节条目")
    
    # 已生成的节文件集合 (使用完整格式 ch_num-sec_num)
    existing = set()
    for sec_num, sec_title, fn, ch_num, ch_title in section_info:
        existing.add((ch_num, sec_num))
    
    # 找出缺失的节
    missing = []
    for ch_num, sec_num, sec_title in toc_entries:
        if (ch_num, sec_num) not in existing:
            missing.append((ch_num, sec_num, sec_title))
    
    if missing:
        print(f"  发现 {len(missing)} 个缺失节:")
        for ch_num, sec_num, sec_title in missing:
            print(f"    第{ch_num}章 § {sec_num} {sec_title}")
    else:
        print("  无缺失节")
    
    return missing


def extract_and_create_missing_sections(merged_path, sections_dir, missing_sections, book_name, column=""):
    """从合并文档中提取缺失节的内容并创建文件"""
    import re
    
    if not missing_sections:
        return 0
    
    with open(merged_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    lines = content.split('\n')
    
    # 找到所有节标题的位置
    section_positions = []  # (line_idx, ch_num, sec_num, title)
    for i, line in enumerate(lines):
        s = line.strip()
        # 匹配各种节标题格式：支持 "1-2"、"1- 2"、"1.2" 等
        m = re.match(r'^##\s*(?:§\s*)?(\d+)\s*[-.]\s*(\d+)\s+(.+)$', s)
        if m:
            ch_num = int(m.group(1))
            sec_num = f"{ch_num}-{int(m.group(2))}"  # 完整格式：6-1
            title = m.group(3).strip()
            section_positions.append((i, ch_num, sec_num, title))
    
    if not section_positions:
        print("  合并文档中未找到节标题，无法提取")
        return 0
    
    created = 0
    for ch_num, sec_num, sec_title in missing_sections:
        # 找到该节的起始行
        start_idx = None
        for pos in section_positions:
            if pos[1] == ch_num and pos[2] == sec_num:
                start_idx = pos[0]
                break
        
        if start_idx is None:
            print(f"  警告: 合并文档中未找到 § {sec_num} {sec_title}")
            continue
        
        # 找到下一节的起始行作为结束
        end_idx = len(lines)
        for pos in section_positions:
            if pos[0] > start_idx:
                end_idx = pos[0]
                break
        
        # 提取内容
        section_lines = lines[start_idx:end_idx]
        section_content = '\n'.join(section_lines)
        
        # 生成文件名
        from split_sections import sanitize
        safe_title = sanitize(sec_title)
        fn = f"{sec_num} {safe_title}.md"
        filepath = os.path.join(sections_dir, fn)
        
        # 添加 frontmatter
        frontmatter = f"""---
title: "{sec_title}"
---

"""
        full_content = frontmatter + section_content
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(full_content)
        
        print(f"  [补全] {fn} ({len(section_lines)} 行)")
        created += 1
    
    return created


def main():
    parser = argparse.ArgumentParser(
        description="Markdown 全流程: 合并 → 分割 → frontmatter 元数据")
    parser.add_argument("--dirs", help="逗号分隔的 PDF 导出文件夹列表 (省略则自动发现)")
    parser.add_argument("--root", default="output", help="自动发现时的搜索根目录 (默认 output/)")
    parser.add_argument("--book", default="", help="书名 (如 电动力学导论)")
    parser.add_argument("--author", default="", help="作者名 (如 格里菲斯); 已废弃，不再用于 column 字段")
    parser.add_argument("--out-root", required=True, help="输出根目录 (如 processed/电动力学导论)")
    parser.add_argument("--split-level", type=int, default=2,
                        help="拆分级别: 1=章, 2=章+节, 3=章+节+小节 (默认2)")
    parser.add_argument("--merged-name", default="", help="合并后的文件名 (默认: {book}.md)")
    parser.add_argument("--sections-dir", default="sections", help="拆分输出目录名 (默认 sections)")
    parser.add_argument("--overwrite-images", action="store_true", help="同名图片强制覆盖")
    args = parser.parse_args()

    os.makedirs(args.out_root, exist_ok=True)

    # 预先计算 sections 目录路径
    sections_dir = os.path.join(args.out_root, args.sections_dir)
    images_dir = os.path.join(sections_dir, "images")

    # ---------- 步骤 1: 合并 ----------
    print("=" * 60)
    print("步骤 1/5: 合并 full.md 与 images")
    print("=" * 60)
    merge_mod = load_module("merge_markdown", "merge_markdown.py")

    if args.dirs:
        folder_list = [os.path.abspath(p.strip()) for p in args.dirs.split("|") if p.strip()]
        for f in folder_list[:]:  # 使用副本迭代，避免修改时出错
            if not os.path.isfile(os.path.join(f, "full.md")):
                print(f"警告: {f} 下无 full.md, 跳过")
                folder_list.remove(f)
        # 保持用户指定的顺序，不再按 part 号排序
    else:
        folder_list = merge_mod.find_source_folders(args.root)
        if not folder_list:
            print(f"在 {args.root} 下未找到包含 full.md 的文件夹")
            return 1

    print(f"发现 {len(folder_list)} 个文件夹:")
    for f in folder_list:
        print(f"  - {f}")

    # 合并文件名: 优先用 --merged-name, 否则用 {book}.md
    merged_name = args.merged_name or (args.book + ".md" if args.book else "merged.md")
    merged_path = os.path.join(args.out_root, merged_name)
    # 图片放在 sections/images/ 下，与章节文件同级
    os.makedirs(images_dir, exist_ok=True)
    merge_mod.merge_markdown(folder_list, merged_path, images_dir, args.overwrite_images)

    # ---------- 步骤 2: 分割 ----------
    print("\n" + "=" * 60)
    print("步骤 2/5: 按章节分割")
    print("=" * 60)
    split_mod = load_module("split_sections", "split_sections.py")

    book_prefix = args.book or os.path.splitext(merged_name)[0]
    # column 格式已废弃，不再使用
    column = ""
    section_info = split_mod.split_document(
        merged_path,
        sections_dir,
        split_level=args.split_level,
        book_name=book_prefix,
        skip_frontmatter=True,
    )

    # ---------- 步骤 3: frontmatter ----------
    print("\n" + "=" * 60)
    print("步骤 3/5: 添加 frontmatter (title)")
    print("=" * 60)
    fm_mod = load_module("add_frontmatter", "add_frontmatter.py")

    fm_mod.process_dir(sections_dir)

    # ---------- 步骤 4: 生成 index.md 目录 ----------
    print("\n" + "=" * 60)
    print("步骤 4/5: 生成 index.md 目录")
    print("=" * 60)
    generate_index(args.out_root, sections_dir, section_info, column)

    # ---------- 步骤 5: 检查并补全缺失章节 ----------
    print("\n" + "=" * 60)
    print("步骤 5/5: 对照目录检查并补全缺失章节")
    print("=" * 60)
    print(f"  DEBUG: section_info length = {len(section_info)}")
    if section_info:
        print(f"  DEBUG: first entry = {section_info[0]}")
    missing = find_missing_sections(merged_path, sections_dir, section_info)
    if missing:
        created = extract_and_create_missing_sections(merged_path, sections_dir, missing, args.book, "")
        print(f"  补全完成: 新增 {created} 个节文件")
        # 重新生成 index.md 包含新增的节
        # 重新读取 sections 目录获取完整列表
        import glob
        all_md = glob.glob(os.path.join(sections_dir, "*.md"))
        # 这里简化处理：重新运行 generate_index 需要完整的 section_info
        # 暂时跳过，用户可手动重跑或后续优化
    else:
        print("  无需补全")

    print("\n" + "=" * 60)
    print("全流程完成!")
    print(f"  合并文件:  {merged_path}")
    print(f"  图片目录:  {images_dir}")
    print(f"  章节文件:  {sections_dir} (含 frontmatter)")
    print(f"  目录文件:  {os.path.join(args.out_root, 'index.md')}")
    print("=" * 60)
    return 0


if __name__ == "__main__":
    sys.exit(main())