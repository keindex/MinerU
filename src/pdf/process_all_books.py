#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""逐本书处理所有 PDF 导出文件夹"""
import os
import sys
sys.path.insert(0, "src/process_md")

# 每本书的文件夹列表（绝对路径）
BOOKS = {
    "场论_朗道": [
        "output/场论 (Л.Д.朗道 (L. D. Landau) etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part1.pdf-949460dd-9ee1-4f31-915e-d78d1f4a8540",
        "output/场论 (Л.Д.朗道 (L. D. Landau) etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part2.pdf-bc2ffcea-da8b-45b9-8e96-45e95369769d",
        "output/场论 (Л.Д.朗道 (L. D. Landau) etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part3.pdf-000c447a-e798-4641-98cd-e010a815bfc8",
    ],
    "弹性理论_朗道": [
        "output/弹性理论 (L. D. Landau etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part1.pdf-0f12cd11-f049-4171-b076-b22b890e09a0",
        "output/弹性理论 (L. D. Landau etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part2.pdf-6aacf752-29b6-47a1-a5e6-d70ca1824904",
    ],
    "流体动力学_朗道": [
        "output/流体动力学 (L. D. Landau etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part1.pdf-b7578cc2-e61b-400f-af7d-9b335933667c",
        "output/流体动力学 (L. D. Landau etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part2.pdf-b36616b3-9644-474d-adcc-d329af07854c",
        "output/流体动力学 (L. D. Landau etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part3.pdf-9eebebc8-4a2f-416a-a650-2f7b97b1ea92",
        "output/流体动力学 (L. D. Landau etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part4.pdf-82962e20-2c20-4003-bd05-24f9f88f6417",
    ],
    "统计物理学I_朗道": [
        "output/统计物理学 I(Statistical Physics, Part 1) (列夫·达维多维奇·朗道 (作者),_ E.M.栗弗席兹 (作者) etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part1.pdf-41134b2d-258e-4cb2-8a85-3289dc6ca174",
        "output/统计物理学 I(Statistical Physics, Part 1) (列夫·达维多维奇·朗道 (作者),_ E.M.栗弗席兹 (作者) etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part2.pdf-965805e4-27b7-4b00-91ba-ccb85781facc",
        "output/统计物理学 I(Statistical Physics, Part 1) (列夫·达维多维奇·朗道 (作者),_ E.M.栗弗席兹 (作者) etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part3.pdf-b0c7812c-3824-471d-9e09-358c7843e06d",
    ],
    "统计物理学II_凝聚态理论": [
        "output/统计物理学II凝聚态理论 ((俄)E.M.粟弗席兹, (俄)л.п.皮塔耶夫斯基 著, 王锡绂 译) (z-library.sk, 1lib.sk, z-lib.sk)_part1.pdf-6a8efd8e-1caa-474f-b750-3fe5844f7d18",
        "output/统计物理学II凝聚态理论 ((俄)E.M.粟弗席兹, (俄)л.п.皮塔耶夫斯基 著, 王锡绂 译) (z-library.sk, 1lib.sk, z-lib.sk)_part2.pdf-1772f2bd-44e2-4f24-91c1-cf963895b5b5",
    ],
    "量子力学与路径积分": [
        "output/量子力学与路径积分 ( etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part1.pdf-5cbf24a2-920a-4101-a511-1b90aeb4d8cd",
        "output/量子力学与路径积分 ( etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part2.pdf-bb8e8a22-bfdf-4287-9318-60cb8fa806a6",
    ],
    "量子力学概论_格里菲斯": [
        "output/量子力学概论 翻译版 原书第3版 (高清带页码) (大卫·J. 格里菲斯) (z-library.sk, 1lib.sk, z-lib.sk)_part1.pdf-9ece73b4-a095-43d8-9129-19a3398855b7",
        "output/量子力学概论 翻译版 原书第3版 (高清带页码) (大卫·J. 格里菲斯) (z-library.sk, 1lib.sk, z-lib.sk)_part2.pdf-d51add08-08fd-4d24-9137-a46e4d766eec",
        "output/量子力学概论 翻译版 原书第3版 (高清带页码) (大卫·J. 格里菲斯) (z-library.sk, 1lib.sk, z-lib.sk)_part3.pdf-c74fcb0f-8f74-4a5a-b7ed-81e564dcbd6f",
    ],
    "量子力学第二卷_科恩塔诺吉": [
        "output/量子力学（第二卷） (Claude Cohen-Tannoudji, Bernard Diu etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part1.pdf-6701f141-bde4-432c-adb5-4687981a3bde",
        "output/量子力学（第二卷） (Claude Cohen-Tannoudji, Bernard Diu etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part2.pdf-12ae2eeb-05be-461d-b2d9-110beaa8f26b",
        "output/量子力学（第二卷） (Claude Cohen-Tannoudji, Bernard Diu etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part3.pdf-9fff6dbb-9887-42f3-bcba-20de7943fda5",
        "output/量子力学（第二卷） (Claude Cohen-Tannoudji, Bernard Diu etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part4.pdf-b7752259-5f05-4099-ab5a-a02f53a330fa",
    ],
}

if __name__ == "__main__":
    import subprocess
    for book_key, dirs in BOOKS.items():
        out_root = f"processed/{book_key}"
        # 清理旧输出
        import shutil
        if os.path.exists(out_root):
            shutil.rmtree(out_root)
        # 构建 --dirs 参数（用引号包裹整个列表）
        dirs_str = "|".join(dirs)
        cmd = [
            sys.executable, "src/process_md/pipeline.py",
            "--dirs", dirs_str,
            "--book", book_key,
            "--out-root", out_root,
        ]
        print(f"\n{'='*60}")
        print(f"处理: {book_key}")
        print(f"{'='*60}")
        result = subprocess.run(cmd, capture_output=False)
        if result.returncode != 0:
            print(f"  失败 (退出码 {result.returncode})")
        else:
            print(f"  完成")
