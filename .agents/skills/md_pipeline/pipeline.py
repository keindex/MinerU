# -*- coding: utf-8 -*-
"""
Markdown 全流程管道: 预处理(合并) → 分割 → 后处理(frontmatter) 一键完成

使用场景:
  用户发来一系列 PDF 导出文件夹 (每文件夹含 full.md + images/),
  期望得到:
    1. 合并后的完整 markdown
    2. 按章节拆分的独立 md 文件
    3. 每个文件带 title + column 的 frontmatter 元数据

流程:
  步骤1 (merge): 按顺序合并各文件夹 full.md, 并合并 images/ 到目标目录
  步骤2 (split): 按章节层级将合并文件拆分为章/节文件
  步骤3 (frontmatter): 为所有拆分文件添加 title + column 元数据

用法示例:
  python pipeline.py \
      --dirs "folderA,folderB,folderC" \
      --book "电动力学导论" \
      --out-root "C:/output" \
      --split-level 2
"""

import os
import sys
import argparse
import importlib.util

SCRIPT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "scripts")


def load_module(name, filename):
    """从 scripts/ 加载模块"""
    path = os.path.join(SCRIPT_DIR, filename)
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    parser = argparse.ArgumentParser(
        description="Markdown 全流程: 合并 → 分割 → frontmatter 元数据")
    parser.add_argument("--dirs", help="逗号分隔的 PDF 导出文件夹列表 (省略则自动发现)")
    parser.add_argument("--root", default=".", help="自动发现时的搜索根目录 (--dirs 省略时)")
    parser.add_argument("--book", default="", help="书名 (用于 column 字段和输出文件前缀)")
    parser.add_argument("--out-root", required=True, help="输出根目录")
    parser.add_argument("--split-level", type=int, default=2,
                        help="拆分级别: 1=章, 2=章+节, 3=章+节+小节 (默认2)")
    parser.add_argument("--merged-name", default="merged.md", help="合并后的文件名 (默认 merged.md)")
    parser.add_argument("--sections-dir", default="sections", help="拆分输出目录名 (默认 sections)")
    parser.add_argument("--overwrite-images", action="store_true", help="同名图片强制覆盖")
    args = parser.parse_args()

    os.makedirs(args.out_root, exist_ok=True)

    # ---------- 步骤 1: 合并 ----------
    print("=" * 60)
    print("步骤 1/3: 合并 full.md 与 images")
    print("=" * 60)
    merge_mod = load_module("merge_markdown", "merge_markdown.py")

    if args.dirs:
        folder_list = [os.path.abspath(p.strip()) for p in args.dirs.split(",") if p.strip()]
        for f in folder_list:
            if not os.path.isfile(os.path.join(f, "full.md")):
                print(f"警告: {f} 下无 full.md, 跳过")
                folder_list.remove(f)
        folder_list = sorted(folder_list, key=lambda p: (
            merge_mod.group_part_number(os.path.basename(p)) is None,
            merge_mod.group_part_number(os.path.basename(p)) or 0,
        ))
    else:
        folder_list = merge_mod.find_source_folders(args.root)
        if not folder_list:
            print(f"在 {args.root} 下未找到包含 full.md 的文件夹")
            return 1

    print(f"发现 {len(folder_list)} 个文件夹:")
    for f in folder_list:
        print(f"  - {f}")

    merged_path = os.path.join(args.out_root, args.merged_name)
    images_dir = os.path.join(args.out_root, "images")
    os.makedirs(images_dir, exist_ok=True)
    merge_mod.merge_markdown(folder_list, merged_path, images_dir, args.overwrite_images)

    # ---------- 步骤 2: 分割 ----------
    print("\n" + "=" * 60)
    print("步骤 2/3: 按章节分割")
    print("=" * 60)
    split_mod = load_module("split_sections", "split_sections.py")

    sections_dir = os.path.join(args.out_root, args.sections_dir)
    book_prefix = args.book or os.path.splitext(args.merged_name)[0]
    split_mod.split_document(
        merged_path,
        sections_dir,
        split_level=args.split_level,
        book_name=book_prefix,
        skip_frontmatter=True,
    )

    # ---------- 步骤 3: frontmatter ----------
    print("\n" + "=" * 60)
    print("步骤 3/3: 添加 frontmatter (title + column)")
    print("=" * 60)
    fm_mod = load_module("add_frontmatter", "add_frontmatter.py")

    column = args.book or book_prefix
    fm_mod.process_dir(sections_dir, column)

    print("\n" + "=" * 60)
    print("全流程完成!")
    print(f"  合并文件:  {merged_path}")
    print(f"  图片目录:  {images_dir}")
    print(f"  章节文件:  {sections_dir} (含 frontmatter)")
    print("=" * 60)
    return 0


if __name__ == "__main__":
    sys.exit(main())