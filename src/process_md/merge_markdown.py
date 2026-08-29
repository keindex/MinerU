# -*- coding: utf-8 -*-
"""
Markdown 预处理: 合并多个 PDF 导出文件夹的 full.md 与 images 目录

功能:
  1. 按顺序合并多个文件夹中的 full.md 为一个 markdown 文件
  2. 将各文件夹下的 images/ 全部合并到目标 images/ 目录
  3. 验证合并后文档中引用的图片是否齐全

用法:
  python merge_markdown.py \
      --dirs "folderA,folderB,folderC" \
      --output merged.md \
      --images-dir images \
      --root "C:/path/to/root"

说明:
  - 若省略 --dirs: 自动在 --root (默认当前目录) 下发现所有含 full.md 的文件夹
  - 文件夹排序: 优先识别 partN (如 part1of3/part2of3) 按自然顺序, 否则按名称排序
  - 图片重名: 已有同名文件时跳过 (哈希文件名一般不重名); --overwrite 可强制覆盖
"""

import argparse
import os
import re
import shutil

def natural_sort_key(name: str):
    """自然排序键: part2 排在 part10 之前"""
    return [int(t) if t.isdigit() else t for t in re.split(r"(\d+)", name)]

def group_part_number(folder_name: str):
    """从文件夹名提取分卷号, 如 part1of3 -> 1 ; 无法识别返回 None"""
    m = re.search(r"part\s*(\d+)", folder_name, re.IGNORECASE)
    return int(m.group(1)) if m else None

def find_source_folders(root: str):
    """在 root 下发现所有包含 full.md 的文件夹, 并排序
    排序策略:
      - 文件夹名前缀相同的归为一组 (视为同一本书的分卷)
      - 组内按 part 号排序; 无 part 号的在前缀组内自然排序
      - 组间按前缀名排序
    """
    folders = []
    for entry in os.listdir(root):
        full_md = os.path.join(root, entry, "full.md")
        if os.path.isdir(os.path.join(root, entry)) and os.path.isfile(full_md):
            folders.append(os.path.join(root, entry))

    def group_key(p):
        """提取前缀分组: part1of3 -> 去掉 'partN' 后的部分"""
        name = os.path.basename(p)
        return re.sub(r"part\s*\d+(?:of\s*\d+)?", "", name, flags=re.IGNORECASE).strip("_")

    def sort_key(p):
        name = os.path.basename(p)
        pn = group_part_number(name)
        return (0, pn) if pn is not None else (1, natural_sort_key(name))

    return sorted(folders, key=lambda p: (group_key(p), sort_key(p)))

def merge_markdown(folder_list, output_path, images_dir, overwrite=False):
    """合并 full.md 与 images"""
    merged_parts = []
    copied, skipped = 0, 0
    total_images_ref = set()

    for i, folder in enumerate(folder_list, 1):
        name = os.path.basename(folder)
        # --- 合并 full.md ---
        md_path = os.path.join(folder, "full.md")
        with open(md_path, "r", encoding="utf-8") as f:
            content = f.read()
        merged_parts.append(content)
        print(f"[{i}] 合并 Markdown: {name} ({len(content.splitlines())} 行)")

        # --- 合并 images ---
        src_img = os.path.join(folder, "images")
        if os.path.isdir(src_img):
            for fn in sorted(os.listdir(src_img)):
                src = os.path.join(src_img, fn)
                if not os.path.isfile(src):
                    continue
                dst = os.path.join(images_dir, fn)
                if os.path.exists(dst) and not overwrite:
                    skipped += 1
                    continue
                shutil.copy2(src, dst)
                copied += 1
                total_images_ref.add(fn)
        else:
            print(f"  警告: {name} 下无 images 目录")

    # --- 写出合并后的 markdown ---
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(merged_parts))
    print(f"\n合并完成: {output_path} ({len(merged_parts)} 个文件)")

    # --- 验证图片引用 ---
    with open(output_path, "r", encoding="utf-8") as f:
        merged_content = f.read()
    refs = set(re.findall(r"!\[[^\]]*\]\(([^)]+)\)", merged_content))
    local_refs = set()
    for r in refs:
        # 只检查相对 images/ 路径的引用
        if r.startswith("images/") or r.startswith("./images/"):
            local_refs.add(os.path.basename(r))

    missing = [r for r in local_refs if r not in total_images_ref and
               not os.path.exists(os.path.join(images_dir, r))]
    print(f"图片: 复制 {copied}, 跳过 {skipped} (已存在)")
    print(f"引用检查: 文档引用图片 {len(local_refs)} 个, 缺失 {len(missing)} 个")
    for m in missing[:20]:
        print(f"  缺失: {m}")
    return merged_parts

def main():
    parser = argparse.ArgumentParser(description="合并多个 PDF 导出文件夹的 full.md 与 images")
    parser.add_argument("--dirs", help="逗号分隔的文件夹列表 (省略则自动发现)")
    parser.add_argument("--output", default="merged.md", help="输出 markdown 文件名")
    parser.add_argument("--images-dir", default="images", help="合并图片输出目录 (相对输出文件位置)")
    parser.add_argument("--root", default=".", help="自动发现时的搜索根目录")
    parser.add_argument("--overwrite", action="store_true", help="同名图片强制覆盖")
    args = parser.parse_args()

    if args.dirs:
        folder_list = [os.path.abspath(p.strip()) for p in args.dirs.split(",") if p.strip()]
    else:
        folder_list = find_source_folders(args.root)
        if not folder_list:
            print(f"在 {args.root} 下未找到包含 full.md 的文件夹")
            return

    for f in folder_list:
        if not os.path.isfile(os.path.join(f, "full.md")):
            print(f"跳过 (无 full.md): {f}")
            folder_list.remove(f)

    print(f"发现 {len(folder_list)} 个文件夹:")
    for f in folder_list:
        print(f"  - {f}")

    images_dir = os.path.join(os.path.dirname(os.path.abspath(args.output)), args.images_dir)
    os.makedirs(images_dir, exist_ok=True)
    merge_markdown(folder_list, args.output, images_dir, args.overwrite)

if __name__ == "__main__":
    main()