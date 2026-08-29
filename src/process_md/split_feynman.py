# -*- coding: utf-8 -*-
"""
费曼《量子电动力学讲义》专用分割脚本

结构特点:
  - 6 个大部分（# 标题）
  - 31 个讲（## 第 N 讲，相当于章）
  - 每讲下有多个小节（## 节名，无编号）
  - 最后有附录（A.1, A.2, A.3）

输出:
  - 每个讲作为一个文件（包含该讲下的所有小节）
  - 文件名格式: {讲号} {讲标题}.md
  - 附录单独处理
"""

import re
import os
import sys

# Windows 控制台 UTF-8
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except (AttributeError, ValueError):
    pass


def sanitize(name: str) -> str:
    """清理文件名中的非法字符"""
    name = re.sub(r"[$^{}]", "", name)
    name = re.sub(r"[\\/:*?\"<>|]", "_", name)
    name = re.sub(r"\s+", " ", name).strip()
    name = name.replace(" ", "_")
    name = re.sub(r"\_+", "_", name)
    name = re.sub(r"[0-9]+$", "", name)
    name = name.strip("_")
    return name


def split_feynman(input_file, output_dir):
    """分割费曼《量子电动力学讲义》"""
    with open(input_file, "r", encoding="utf-8") as f:
        content = f.read()

    lines = content.split("\n")

    # 找出所有标题
    headers = []
    for i, line in enumerate(lines):
        s = line.strip()
        if s.startswith("#"):
            headers.append((i, s))

    # 找到第一个 # 部分标题（正文开始）
    first_part_idx = None
    for idx, (line_idx, header) in enumerate(headers):
        if header.startswith("# ") and not header.startswith("##"):
            first_part_idx = idx
            break

    # 找到附录开始
    appendix_idx = None
    for idx, (line_idx, header) in enumerate(headers):
        if header.startswith("## A. 附录") or header.startswith("## 附录"):
            appendix_idx = idx
            break

    # 处理正文部分
    body_headers = headers[first_part_idx:appendix_idx] if appendix_idx else headers[first_part_idx:]

    # 识别讲和节
    lectures = []  # (line_idx, lecture_num)
    sections = []  # (line_idx, lecture_num, section_title)

    current_lecture = None
    for line_idx, header in body_headers:
        # 匹配 '## 第 N 讲' 或 '## 第N讲'
        m = re.match(r"^##\s*第\s*(\d+)\s*讲\s*$", header)
        if m:
            current_lecture = int(m.group(1))
            lectures.append((line_idx, current_lecture))
            continue

        # 跳过 # 标题（部分标题）
        if header.startswith("# ") and not header.startswith("##"):
            continue

        # 匹配 '## 第 N 讲' 后面的节标题
        if current_lecture is not None:
            # 跳过中文数字章节标记
            if re.match(r"^##\s*[一二三四五六七八九十]+、\s*$", header):
                continue
            # 跳过附录相关
            if header.startswith("## A.") or header.startswith("## 附录") or header.startswith("## 附注"):
                continue
            # 跳过单字母标题
            if re.match(r"^##\s+[A-Za-z]\.\s", header):
                continue
            # 跳过数字编号标题
            if re.match(r"^##\s+\d+\.\s", header):
                continue
            # 跳过小写字母标题
            if re.match(r"^##\s+[a-z]\.\s", header):
                continue

            # 这是一个节标题
            sections.append((line_idx, current_lecture, header))

    # 为每个讲分配节索引
    from collections import defaultdict
    lecture_sections = defaultdict(list)
    for line_idx, lecture_num, section_title in sections:
        lecture_sections[lecture_num].append((line_idx, section_title))

    # 确定每个讲的内容范围
    lecture_ranges = {}  # lecture_num -> (start_line, end_line)
    for i, (line_idx, lecture_num) in enumerate(lectures):
        start = line_idx
        if i + 1 < len(lectures):
            end = lectures[i + 1][0]
        else:
            # 最后一个讲的范围到附录开始
            if appendix_idx is not None:
                end = headers[appendix_idx][0]
            else:
                end = len(lines)
        lecture_ranges[lecture_num] = (start, end)

    # 确定每个节的内容范围
    section_ranges = []  # (lecture_num, section_idx, section_title, start_line, end_line)
    for lecture_num in sorted(lecture_sections.keys()):
        secs = lecture_sections[lecture_num]
        lecture_start, lecture_end = lecture_ranges[lecture_num]
        for j, (line_idx, section_title) in enumerate(secs):
            start = line_idx
            if j + 1 < len(secs):
                end = secs[j + 1][0]
            else:
                end = lecture_end
            section_ranges.append((lecture_num, j + 1, section_title, start, end))

    # 处理没有节的讲
    for lecture_num in sorted(lecture_ranges.keys()):
        if lecture_num not in lecture_sections:
            lecture_start, lecture_end = lecture_ranges[lecture_num]
            section_ranges.append((lecture_num, 0, "", lecture_start, lecture_end))

    # 排序
    section_ranges.sort(key=lambda x: (x[0], x[1]))

    # 处理附录
    if appendix_idx is not None:
        appendix_start = headers[appendix_idx][0]
        # 找到附录下的所有小节
        appendix_sections = []
        for i in range(appendix_idx + 1, len(headers)):
            line_idx, header = headers[i]
            if header.startswith("## A.") and re.match(r"^##\s+A\.\d+\s+", header):
                appendix_sections.append((line_idx, header))
            elif header.startswith("# ") and not header.startswith("##"):
                break
        
        for j, (line_idx, section_title) in enumerate(appendix_sections):
            start = line_idx
            if j + 1 < len(appendix_sections):
                end = appendix_sections[j + 1][0]
            else:
                end = len(lines)
            section_ranges.append((999, j + 1, section_title, start, end))

    # 写出文件
    os.makedirs(output_dir, exist_ok=True)
    written = 0
    section_info = []  # (sec_num, sec_title, fn, ch_num, ch_title)

    for lecture_num, section_idx, section_title, start, end in section_ranges:
        # 提取内容
        section_content = "\n".join(lines[start:end])

        # 生成文件名
        if lecture_num == 999:
            # 附录
            sec_num = f"A.{section_idx}"
            clean_title = re.sub(r"^##\s+", "", section_title).strip()
            safe_title = sanitize(clean_title)
            fn = f"{sec_num} {safe_title}.md"
            ch_num = "A"
            ch_title = "附录"
        elif section_idx == 0:
            # 没有节的讲
            sec_num = f"{lecture_num}"
            clean_title = f"第{lecture_num}讲"
            safe_title = sanitize(clean_title)
            fn = f"{sec_num} {safe_title}.md"
            ch_num = lecture_num
            ch_title = f"第{lecture_num}讲"
        else:
            sec_num = f"{lecture_num}.{section_idx}"
            # 清理节标题（去掉 ## 前缀）
            clean_title = re.sub(r"^##\s+", "", section_title).strip()
            # 去掉 LaTeX 标记
            clean_title = re.sub(r"\$\^{(\d+)}\$", "", clean_title)
            clean_title = re.sub(r"\$", "", clean_title)
            clean_title = clean_title.strip()
            safe_title = sanitize(clean_title)
            fn = f"{sec_num} {safe_title}.md"
            ch_num = lecture_num
            ch_title = f"第{lecture_num}讲"

        filepath = os.path.join(output_dir, fn)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(section_content)
        written += 1
        print(f"  [节] {fn} ({end - start} 行)")

        section_info.append((sec_num, clean_title, fn, ch_num, ch_title))

    print(f"\n完成! 共创建 {written} 个文件于 {output_dir}")
    return section_info


def main():
    parser = __import__("argparse").ArgumentParser(description="费曼《量子电动力学讲义》专用分割脚本")
    parser.add_argument("--input", required=True, help="输入 markdown 文件")
    parser.add_argument("--output-dir", required=True, help="输出目录")
    args = parser.parse_args()

    split_feynman(args.input, args.output_dir)


if __name__ == "__main__":
    main()
