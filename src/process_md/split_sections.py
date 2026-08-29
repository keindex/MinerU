# -*- coding: utf-8 -*-
"""
通用 Markdown 章节分割器: 将长篇 Markdown 按章节层级拆分为独立文件

设计 (泛化自 markdown-section-splitter / split_ied.py):

支持的标题层级 (自动识别):
  - 章:  `## 第 X 章 章名`            (level 1)
  - 节:  `## X.Y 节名`                (level 2)
  - 小节: `## X.Y.Z 小节名`            (level 3, 归入节, 不单独建文件)
  - 罗马数字章: `## I. INTRODUCTION`   (level 1)
  - 字母节: `### A. 标题`              (level 2)

拆分级别 (用户可指定):
  - 第 1 级: 仅拆出章文件
  - 第 2 级: 章 + 节
  - 第 3 级: 章 + 节 + 小节

需要删除的内容:
  1. 前置部分: 封面/作者/出版/目录/序言 (第一个章标题之前)
  2. 附录/索引 (附录/Appendix 起至文末)
  3. 乱码/噪声标题 (如单字母 "B", "C", "D" 等索引条目)

命名规则:
  - 节文件:   {sec_num} {sec_title}.md (如 1.1 Coulomb's_Law.md)
  - 章文件:   不再单独输出 (内容归入其下第一个节文件)
  特殊字符 (\\ / : * ? " < > |) 替换为 _, LaTeX 符号清理
"""

import re
import os
import argparse
import io
import sys

# Windows 控制台默认 GBK, 显式使用 UTF-8 输出避免中文打印乱码/报错
# (仅当未被包装时进行; 在 pipeline 中作为模块加载时 stdout 可能已包装)
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except (AttributeError, ValueError):
    pass

# 缺失的章标题 -> 章名 (从目录页人工补全; 用于标题缺失的文档)
MISSING_CHAPTER_TITLES = {
    3: "第 3 章 势",
    5: "第 5 章 静磁学",
    7: "第 7 章 电动力学",
    9: "第 9 章 电磁波",
    10: "第 10 章 势与场",
    11: "第 11 章 辐射",
}

# 章标题：支持 "第X章 标题"、"第X章标题"（无空格）、"第X章"（无标题）
CHAPTER_RE = re.compile(r"^#{1,2}\s+(第\s*([0-9一二三四五六七八九十]+)\s*章)\s*(.*)$")
# 补充习题标题 ("第1章补充习题"), 不应被当作章标题
REVIEW_RE = re.compile(r"^##\s*第\s*[0-9一二三四五六七八九十]+\s*章\s*补充习题")
SECTION_RE = re.compile(r"^#{1,2}\s+([IVXLCDM]+|\d+)\.(\d+)\s+(.+)$")
SUBSECTION_RE = re.compile(r"^##\s+([IVXLCDM]+|\d+)\.(\d+)\.(\d+)\s+(.+)$")
# 连字符节号 (如费曼 1-1, 2-3): 一级标题章(# 章名) + 连字符节(## N-M 节名)
# 支持 "1-1"、"1- 1"（数字与连字符间有空格）、"[19] 1-4"（带页码前缀）等格式
SECTION_DASH_RE = re.compile(r"^##\s*(?:\[\d+\]\s*)?(\d+)\s*-\s*(\d+)\s+(.+)$")
# 补充习题节号 (如 2-S1, 5-S1): 用于处理章节末尾的习题
SECTION_SUPP_DASH_RE = re.compile(r"^##\s*(\d+)\s*-\s*S(\d+)\s+(.+)$")
# 费曼 § 格式节号: ## § 1-2 节名
SECTION_FEYNMAN_RE = re.compile(r"^##\s*§\s*(\d+)\s*-\s*(\d+)\s+(.+)$")
# 朗道 § 格式节号: ## §N 节名 (连续编号，不分章)
SECTION_LANDAU_RE = re.compile(r"^##\s*§\s*(\d+)\s+(.+)$")
# 科恩塔诺吉格式：## §A. 标题, ## §B. 标题 (字母编号节)
SECTION_COHENA_RE = re.compile(r"^##\s*§\s*([A-Z])\.\s+(.+)$")
# 科恩塔诺吉格式：## 1. 标题, ## a. 标题 (数字/字母小节)
SECTION_COHENA_NUM_RE = re.compile(r"^##\s+(\d+)\.\s+(.+)$")
SECTION_COHENA_LETTER_RE = re.compile(r"^##\s+([a-z])\.\s+(.+)$")
# 科恩塔诺吉格式补充材料：## 1. 标题 (数字节), ## a. 标题/## α. 标题 (字母/希腊字母小节)
SECTION_SUPP_NUM_RE = re.compile(r"^##\s+(\d+)\.\s+(.+)$")
SECTION_SUPP_LETTER_RE = re.compile(r"^##\s+([a-zαβγδεζηθικλμνξοπρστυφχψω])\.\s+(.+)$")
# 科恩塔诺吉格式章：## 第X章提纲, ## 第X章 章名 (支持带页码前缀如 ## [902] 第八章提纲)
CHAPTER_COHENA_RE = re.compile(r"^##\s*(?:\[\d+\]\s*)?(第\s*([0-9一二三四五六七八九十]+)\s*章)(?:提纲)?\s*(.*)$")
APPENDIX_RE = re.compile(r"^#{1,2}\s*(附录|Appendix|APPENDIX|Index|索引|后记|跋|参考资料|参考文献)\b", re.IGNORECASE)
LETTER_ONLY_RE = re.compile(r"^##\s+([A-Z])\s*$")
ROMAN_CHAPTER_RE = re.compile(r"^#{2,3}\s+([IVXLC]+)\.\s+(\D.+)$")
LETTER_SECTION_RE = re.compile(r"^#{3}\s+([A-Z])\.\s+(.+)$")
# 一级标题 = 章 (如 Jackson: `# Introduction to Electrostatics` + `## 1.1 Coulomb's Law`)
HASH_CHAPTER_RE = re.compile(r"^#\s+([^#].+)$")
# 一级标题章：# 第X章 章名（支持无空格、无标题）
HASH_CHINESE_CHAPTER_RE = re.compile(r"^#\s+(第\s*([0-9一二三四五六七八九十]+)\s*章)\s*(.*)$")


def roman_to_int(s: str):
    """罗马数字转阿拉伯数字 (I->1, IV->4, IX->9 等)"""
    s = s.upper()
    if s.isdigit():
        return int(s)
    vals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    prev = 0
    for ch in reversed(s):
        v = vals.get(ch, 0)
        if v < prev:
            total -= v
        else:
            total += v
            prev = v
    return total


def chinese_to_int(s: str):
    """中文数字转阿拉伯数字 (一->1, 二->2, 十->10, 十一->11, 二十->20, 十三->13 等)"""
    if s.isdigit():
        return int(s)
    # 单字映射
    cn_digits = {
        "零": 0, "一": 1, "二": 2, "三": 3, "四": 4, "五": 5,
        "六": 6, "七": 7, "八": 8, "九": 9, "十": 10,
        "两": 2,  # 两百、两千等
    }
    # 处理 "十"、"二十"、"三十" 等
    if s == "十":
        return 10
    if s.startswith("十"):
        # 十一、十二...
        return 10 + cn_digits.get(s[1], 0)
    if s.endswith("十"):
        # 二十、三十...
        return cn_digits.get(s[0], 1) * 10
    # 处理 "二十五"、"十三" 等（十在中间）
    if "十" in s:
        parts = s.split("十")
        tens = cn_digits.get(parts[0], 1) * 10
        ones = cn_digits.get(parts[1], 0) if parts[1] else 0
        return tens + ones
    # 单字
    return cn_digits.get(s, 0)


def sanitize(name: str) -> str:
    """清理文件名中的非法字符"""
    name = re.sub(r"[$^{}]", "", name)  # 先去掉 LaTeX 符号 (会引入多余下划线)
    name = re.sub(r"[\\/:*?\"<>|]", "_", name)
    name = re.sub(r"\s+", " ", name).strip()
    name = name.replace(" ", "_")        # 空格统一为下划线
    name = re.sub(r"\_+", "_", name)     # 合并多个下划线
    name = re.sub(r"[0-9]+$", "", name)  # 去掉末尾残留的上标数字 (如 $^{12}$ 的 12)
    name = name.strip("_")
    return name


def clean_section_title(title: str) -> str:
    """清理节标题，移除章节号前缀（如 '§ 2-1 '、'1.1 '、'I.1 '、'A. '等）"""
    # 移除 § 格式前缀（费曼：§ 2-1、§ 1-2 等）
    title = re.sub(r"^§\s*\d+\s*-\s*\d+\s+", "", title)
    # 移除朗道 § 格式前缀（§N）
    title = re.sub(r"^§\s*\d+\s+", "", title)
    # 移除标准数字节号前缀（1.1、1.2、I.1、II.2 等）
    title = re.sub(r"^([IVXLCDM]+|\d+)(\.\d+)+\s+", "", title)
    # 移除字母节号前缀（A.、B. 等）
    title = re.sub(r"^[A-Z]\.\s+", "", title)
    # 移除连字符节号前缀（1-1、1- 1、2-3 等，非 § 格式）
    title = re.sub(r"^\d+\s*-\s*\d+\s+", "", title)
    return title.strip()


def clean_content_headers(content: str, clean_sec_title: str, clean_sub_title: str = None) -> str:
    """清理内容中的标题，将带章节号的标题替换为清理后的标题"""
    lines = content.split("\n")
    new_lines = []
    for line in lines:
        stripped = line.strip()
        # 匹配标题行
        m = re.match(r"^(#{1,6})\s+(.+)$", stripped)
        if m:
            level = m.group(1)
            title = m.group(2).strip()
            # 如果标题包含章节号前缀，替换为清理后的标题
            cleaned = clean_section_title(title)
            if cleaned != title:
                # 只有当清理后的标题与目标标题匹配时才替换
                if cleaned == clean_sec_title or (clean_sub_title and cleaned == clean_sub_title):
                    line = f"{level} {cleaned}"
        new_lines.append(line)
    return "\n".join(new_lines)


def split_document(input_file, output_dir, split_level=2, book_name="", skip_frontmatter=True):
    """按章节拆分文档

    Args:
        input_file: 输入 markdown 路径
        output_dir: 输出目录
        split_level: 1/2/3 级
        book_name: 输出文件前缀 (默认取输入文件名)
        skip_frontmatter: 是否跳过 frontmatter (--- ---) 块
    """
    with open(input_file, "r", encoding="utf-8") as f:
        content = f.read()

    # 可选: 移除开头的 frontmatter 块
    if skip_frontmatter:
        content = re.sub(r"^---\n.*?\n---\s*\n?", "", content, flags=re.S)

    lines = content.split("\n")
    if not book_name:
        book_name = os.path.splitext(os.path.basename(input_file))[0]

    # 判断章节模式: 一级标题章(# 标题+数字节) 优先, 其次中文章(第X章), 再次罗马章(I.)
    has_chinese_chapters = any(CHAPTER_RE.match(l.strip()) or HASH_CHINESE_CHAPTER_RE.match(l.strip()) for l in lines)
    has_roman_chapters = any(ROMAN_CHAPTER_RE.match(l.strip()) for l in lines)
    has_hash_chapters = False
    # 检测朗道 § 格式: 一级标题章(# 第X章) + 二级节标题(## §N 节名)
    has_landau_chapters = False
    # 检测科恩塔诺吉格式: ## 第X章提纲 + ## §A. 节名
    has_cohen_chapters = False
    if not has_chinese_chapters and not has_roman_chapters:
        hash_ch_count = sum(1 for l in lines if HASH_CHINESE_CHAPTER_RE.match(l.strip()))
        landau_sec_count = sum(1 for l in lines if SECTION_LANDAU_RE.match(l.strip()))
        has_landau_chapters = hash_ch_count >= 1 and landau_sec_count >= 3
        if has_landau_chapters:
            has_chinese_chapters = True  # 复用中文章处理逻辑（章号从 § 提取）
        
        # 检测科恩塔诺吉格式
        cohen_ch_count = sum(1 for l in lines if CHAPTER_COHENA_RE.match(l.strip()))
        cohen_sec_count = sum(1 for l in lines if SECTION_COHENA_RE.match(l.strip()))
        has_cohen_chapters = cohen_ch_count >= 1 and cohen_sec_count >= 3
        print(f"DEBUG: cohen_ch_count={cohen_ch_count}, cohen_sec_count={cohen_sec_count}, has_cohen_chapters={has_cohen_chapters}")
        if has_cohen_chapters:
            has_chinese_chapters = True  # 复用中文章处理逻辑
    if not has_chinese_chapters:
        # 检测是否有 一级标题(#) + 数字节(## X.Y 或 ## N-M 或 ## § N-M) 的组合
        hash_count = 0
        sec_count = 0
        for l in lines:
            s = l.strip()
            if HASH_CHAPTER_RE.match(s):
                hash_count += 1
            if SECTION_RE.match(s) or SECTION_DASH_RE.match(s) or SECTION_FEYNMAN_RE.match(s):
                sec_count += 1
        # Jackson: 封面 # 标题很多但正文 # 标题少而数字节多 -> 排除封面式小标题干扰
        has_hash_chapters = hash_count >= 2 and sec_count >= 5
        if has_hash_chapters:
            has_roman_chapters = False  # 一级标题模式优先, 禁用罗马章模式

    # ---------- 定位正文起点与附录终点 (独立扫描) ----------
    start_idx = 0
    appendix_idx = len(lines)
    # 先找附录终点 (全文扫描, 任一明确的 附录/索引/Appendix 标题即止)
    # 注意: Special Functions/Key Material 等通用词汇不作附录标记, 否则会误伤正文节名
    # (如 Arfken 第1章的 "## Special Functions" 是正文小节, 却被误判为附录导致截断)
    # "参考资料"、"参考文献"、"后记"、"跋" 可能出现在各章/各册末尾, 只有在文档末尾(最后 5%)且后无章/节标题时才视为附录
    for i, line in enumerate(lines):
        s = line.strip()
        if APPENDIX_RE.match(s):
            # 检查是否为"参考资料"、"参考文献"、"后记"、"跋"
            is_ref = re.match(r"^#{1,2}\s*(参考资料|参考文献|后记|跋)\b", s, re.IGNORECASE)
            if is_ref:
                # 只有在文档最后 5% 且后面没有章/节标题时才视为附录
                if i < len(lines) * 0.95:
                    continue  # 不是文档末尾, 跳过
                # 检查后面是否还有章标题或节标题
                has_chapter_after = False
                for j in range(i + 1, len(lines)):
                    if (CHAPTER_RE.match(lines[j].strip()) or
                        HASH_CHINESE_CHAPTER_RE.match(lines[j].strip()) or
                        SECTION_RE.match(lines[j].strip()) or
                        SECTION_DASH_RE.match(lines[j].strip()) or
                        SECTION_FEYNMAN_RE.match(lines[j].strip())):
                        has_chapter_after = True
                        break
                if has_chapter_after:
                    continue  # 后面还有章/节标题, 不是附录
            appendix_idx = i
            break
    if has_hash_chapters:
        # 一级标题章模式: 从第一个"其后紧跟数字节(## X.Y 或 ## N-M 或 ## § N-M)"的 # 标题开始作为正文起点
        # (跳过封面/序言等非正文 # 标题)
        for i in range(appendix_idx if appendix_idx < len(lines) else len(lines)):
            line = lines[i]
            s = line.strip()
            m = HASH_CHAPTER_RE.match(s)
            if not m:
                continue
            # 检查该 # 标题之后 300 行内是否出现 ## X.Y 数字节 或 ## N-M 连字符节 或 ## § N-M
            for j in range(i + 1, min(i + 300, len(lines))):
                if (SECTION_RE.match(lines[j].strip()) or
                    SECTION_DASH_RE.match(lines[j].strip()) or
                    SECTION_FEYNMAN_RE.match(lines[j].strip())):
                    start_idx = i
                    break
                # 若遇到另一个 # 标题, 说明该标题后无正文, 继续找下一个
                if HASH_CHAPTER_RE.match(lines[j].strip()):
                    break
            if start_idx:
                break
    elif has_cohen_chapters:
        # 科恩塔诺吉格式: 从第一个 ## 第X章提纲 开始作为正文起点
        for i in range(appendix_idx if appendix_idx < len(lines) else len(lines)):
            s = lines[i].strip()
            if CHAPTER_COHENA_RE.match(s):
                start_idx = i
                print(f"DEBUG: start_idx set to {i}, line: {s[:80]}")
                break
    else:
        for i in range(appendix_idx if appendix_idx < len(lines) else len(lines)):
            s = lines[i].strip()
            is_ch = (CHAPTER_RE.match(s) or
                     (has_roman_chapters and ROMAN_CHAPTER_RE.match(s)))
            if start_idx == 0 and is_ch:
                start_idx = i
    if start_idx >= appendix_idx:
        start_idx = 0  # 未找到章标题时从开头处理

    body_lines = lines[start_idx:appendix_idx]

    # ---------- 扫描标题 ----------
    headers = []  # (line_idx_in_body, kind, num, title)
    # kind: 'ch' 章, 'sec' 节, 'sub' 小节(level3)
    for i, line in enumerate(body_lines):
        s = line.strip()
        if not s.startswith("#"):
            continue
        if REVIEW_RE.match(s):
            continue  # 补充习题标题, 归入章文件
        if has_chinese_chapters:
            # 处理标准中文章格式 (## 第X章) 和朗道格式 (# 第X章 + ## §N)
            m = CHAPTER_RE.match(s)
            if m:
                try:
                    ch_num = chinese_to_int(m.group(2))
                except ValueError:
                    ch_num = 0
                headers.append((i, "ch", ch_num, f"{m.group(1)} {m.group(3)}"))
                continue
            # 朗道格式: # 第X章 章名 (一级标题章)
            m = HASH_CHINESE_CHAPTER_RE.match(s)
            if m:
                try:
                    ch_num = chinese_to_int(m.group(2))
                except ValueError:
                    ch_num = 0
                headers.append((i, "ch", ch_num, f"{m.group(1)} {m.group(3)}"))
                continue
            # 科恩塔诺吉格式: ## 第X章提纲, ## 第X章 章名
            m = CHAPTER_COHENA_RE.match(s)
            if m:
                try:
                    ch_num = chinese_to_int(m.group(2))
                    print(f"DEBUG: chinese_to_int('{m.group(2)}') = {ch_num}")
                except ValueError:
                    ch_num = 0
                title = m.group(1) + (m.group(3) if m.group(3) else "")
                headers.append((i, "ch", ch_num, title.strip()))
                continue
            m = SECTION_RE.match(s)
            if m:
                # 中文章格式使用连字符格式 (2-1) 而非点号格式 (2.1)，以匹配目录页格式
                headers.append((i, "sec", f"{int(m.group(1))}-{int(m.group(2))}",
                                (int(m.group(1)), m.group(3))))
                continue
            # 补充习题节号: ## N-S1 节名 (如 2-S1, 5-S1)
            m = SECTION_SUPP_DASH_RE.match(s)
            if m:
                headers.append((i, "sec", f"{int(m.group(1))}-S{int(m.group(2))}",
                                (int(m.group(1)), m.group(3))))
                continue
            # 费曼 § 格式节号: ## § 1-2 节名
            m = SECTION_FEYNMAN_RE.match(s)
            if m:
                headers.append((i, "sec", f"{int(m.group(1))}-{int(m.group(2))}",
                                (int(m.group(1)), m.group(3))))
                continue
            # 朗道 § 格式节号: ## §N 节名 (连续编号)
            m = SECTION_LANDAU_RE.match(s)
            if m:
                sec_num = int(m.group(1))
                # 朗道格式的节号是连续编号，需要根据前面的章来确定章节号
                # 这里先简单处理：用节号本身作为 sec_num，后续根据章节边界分配
                headers.append((i, "sec", f"§{sec_num}",
                                (sec_num, m.group(2))))
                continue
            # 科恩塔诺吉格式节：## §A. 标题, ## §B. 标题 (字母编号)
            m = SECTION_COHENA_RE.match(s)
            if m:
                letter = m.group(1)
                sec_num = f"§{letter}"
                headers.append((i, "sec", sec_num, (ord(letter) - ord('A') + 1, m.group(2))))
                continue
            # 科恩塔诺吉格式小节：## 1. 标题, ## a. 标题
            m = SECTION_COHENA_NUM_RE.match(s)
            if m:
                headers.append((i, "sub", m.group(1), (int(m.group(1)), m.group(2))))
                continue
            m = SECTION_COHENA_LETTER_RE.match(s)
            if m:
                headers.append((i, "sub", m.group(1), (ord(m.group(1)) - ord('a') + 1, m.group(2))))
                continue
            # 补充材料格式：## 1. 标题 (数字节), ## a. 标题/## α. 标题 (字母/希腊字母小节)
            m = SECTION_SUPP_NUM_RE.match(s)
            if m:
                headers.append((i, "sec", m.group(1), (int(m.group(1)), m.group(2))))
                continue
            m = SECTION_SUPP_LETTER_RE.match(s)
            if m:
                # 小节号直接使用匹配到的字母（包括希腊字母）
                headers.append((i, "sub", m.group(1), (m.group(1), m.group(2))))
                continue
            if split_level >= 3:
                m = SUBSECTION_RE.match(s)
                if m:
                    # 中文章格式使用连字符格式 (2-1-1) 而非点号格式 (2.1.1)
                    headers.append((i, "sub", f"{int(m.group(1))}-{int(m.group(2))}-{int(m.group(3))}",
                                    (int(m.group(1)), m.group(4))))
                    continue
        elif has_roman_chapters:
            m = ROMAN_CHAPTER_RE.match(s)
            if m:
                headers.append((i, "ch", m.group(1), f"{m.group(1)}. {m.group(2)}"))
                continue
            m = LETTER_SECTION_RE.match(s)
            if m:
                headers.append((i, "sec", m.group(1), (m.group(1), m.group(2))))
                continue
        elif has_hash_chapters:
            m = HASH_CHAPTER_RE.match(s)
            if m and m.group(1).strip():
                # 跳过封面/摘要/前言等非正文一级标题 (在第一个数字节之前的 # 不算章)
                headers.append((i, "ch", len([h for h in headers if h[1] == "ch"]) + 1, m.group(1).strip()))
                continue
            # 连字符节 (费曼 1-1): 属于 # 章下的节
            m = SECTION_DASH_RE.match(s)
            if m:
                ch_num = int(m.group(1))
                headers.append((i, "sec", f"{m.group(1)}-{int(m.group(2))}",
                                (ch_num, m.group(3))))
                continue
            # 费曼 § 格式节号: ## § 1-2 节名
            m = SECTION_FEYNMAN_RE.match(s)
            if m:
                ch_num = int(m.group(1))
                headers.append((i, "sec", f"{m.group(1)}-{int(m.group(2))}",
                                (ch_num, m.group(3))))
                continue
            m = SECTION_RE.match(s)
            if m:
                ch_num = roman_to_int(m.group(1))
                headers.append((i, "sec", f"{m.group(1)}.{int(m.group(2))}",
                                (ch_num, m.group(3))))
                continue
            if split_level >= 3:
                m = SUBSECTION_RE.match(s)
                if m:
                    ch_num = roman_to_int(m.group(1))
                    headers.append((i, "sub", f"{m.group(1)}.{int(m.group(2))}.{int(m.group(3))}",
                                    (ch_num, m.group(4))))
                    continue
        # 其他标题忽略
        if LETTER_ONLY_RE.match(s):
            continue  # 索引单字母条目

    headers.sort(key=lambda h: h[0])

    # ---------- 构建章边界 ----------
    # 显式章标题缺失时(文档直接从 "## 3.1" 开始), 用节标题推断章边界并补全章名
    chapters = []  # (start, end, ch_num, ch_title)
    if has_chinese_chapters:
        # 检测是否为朗道格式 (# 第X章 + ## §N)
        is_landau_format = has_landau_chapters or any(h[1] == "sec" and h[2].startswith("§") and h[2][1:].isdigit() for h in headers)
        # 检测是否为科恩塔诺吉格式 (## 第X章提纲 + ## §A. 节名)
        is_cohen_format = has_cohen_chapters or any(h[1] == "sec" and h[2].startswith("§") and len(h[2]) == 2 and h[2][1].isalpha() for h in headers)
        
        print(f"DEBUG: is_landau_format={is_landau_format}, is_cohen_format={is_cohen_format}")
        print(f"DEBUG: headers count={len(headers)}")
        ch_headers_debug = [h for h in headers if h[1] == "ch"]
        print(f"DEBUG: ch_headers count={len(ch_headers_debug)}")
        for h in ch_headers_debug:
            print(f"  {h}")
        
        if is_landau_format:
            # 朗道格式：章由 # 第X章 定义，节由 ## §N 定义（连续编号）
            # 收集所有显式章标题
            ch_headers = [h for h in headers if h[1] == "ch"]
            sec_headers = [h for h in headers if h[1] == "sec"]
            
            for ci, h in enumerate(ch_headers):
                ch_num = h[2]
                ch_title = h[3]
                start = h[0]
                end = ch_headers[ci + 1][0] if ci + 1 < len(ch_headers) else len(body_lines)
                chapters.append((start, end, ch_num, ch_title))
            
            # 如果没有显式章标题，退回到整个文档作为一章
            if not chapters:
                chapters.append((0, len(body_lines), 1, "正文"))
        elif is_cohen_format:
            # 科恩塔诺吉格式：章由 ## 第X章提纲 定义，节由 ## §A. 定义（字母编号）
            ch_headers = [h for h in headers if h[1] == "ch"]
            
            for ci, h in enumerate(ch_headers):
                ch_num = h[2]
                ch_title = h[3]
                start = h[0]
                end = ch_headers[ci + 1][0] if ci + 1 < len(ch_headers) else len(body_lines)
                chapters.append((start, end, ch_num, ch_title))
            
            if not chapters:
                chapters.append((0, len(body_lines), 1, "正文"))
        else:
            # 标准中文章格式
            # 收集所有显式章和所有节标题的章号, 确定每章的起止
            all_ch_nums = sorted(set(
                [h[2] for h in headers if h[1] == "ch"] + [h[3][0] for h in headers if h[1] == "sec"]
            ))
            # 每章起点: 显式章标题优先, 否则该章第一个节标题
            bound_map = {}  # ch_num -> (start_line, ch_title)
            for h in headers:
                if h[1] == "ch" and h[2] not in bound_map:
                    bound_map[h[2]] = (h[0], h[3])
            for n in all_ch_nums:
                if n not in bound_map:
                    first_sec = next((hh for hh in headers if hh[1] == "sec" and hh[3][0] == n), None)
                    if first_sec is None:
                        continue
                    bound_map[n] = (first_sec[0], MISSING_CHAPTER_TITLES.get(n, f"第 {n} 章"))
            # 按行号排序确定边界
            bounds = sorted(bound_map.items(), key=lambda kv: kv[1][0])
            for bi, (n, (start, title)) in enumerate(bounds):
                end = bounds[bi + 1][1][0] if bi + 1 < len(bounds) else len(body_lines)
                chapters.append((start, end, n, title))
    elif has_roman_chapters:
        ch_indices = [i for i, h in enumerate(headers) if h[1] == "ch"]
        for ci, hi in enumerate(ch_indices):
            start = headers[hi][0]
            end = headers[ch_indices[ci + 1]][0] if ci + 1 < len(ch_indices) else len(body_lines)
            chapters.append((start, end, headers[hi][2], headers[hi][3]))
    elif has_hash_chapters:
        # 一级标题章: 按行号顺序切分 (# 章 -> 下一个 # 章)
        ch_indices = [i for i, h in enumerate(headers) if h[1] == "ch"]
        for ci, hi in enumerate(ch_indices):
            start = headers[hi][0]
            end = headers[ch_indices[ci + 1]][0] if ci + 1 < len(ch_indices) else len(body_lines)
            chapters.append((start, end, headers[hi][2], headers[hi][3]))
    else:
        # 无章结构: 整个文件作为一个章
        chapters.append((0, len(body_lines), 1, "正文"))

    print(f"找到 {len(chapters)} 章")
    for c in chapters:
        print(f"  章 {c[2]}: {c[3]} (行 {c[0] + 1}~{c[1]})")

    # ---------- 提取节 (支持 level2/3) ----------
    sections = []  # (ch_num, ch_title, sec_num, sec_title, sub_num, sub_title, start, sub_start, end)
    if split_level >= 2:
        for ch_start, ch_end, ch_num, ch_title in chapters:
            if has_roman_chapters or has_hash_chapters:
                # 罗马/一级标题结构: 章下节按行号范围
                ch_secs = [h for h in headers if h[1] in ("sec", "sub") and ch_start <= h[0] < ch_end]
            else:
                # 中文章: 用章号匹配 (缺失章标题时按节号分组)
                ch_secs = [h for h in headers
                           if h[1] in ("sec", "sub") and h[0] >= ch_start and h[0] < ch_end]
            # 只取 sec 级别作为拆分点 (sub 归入其上一级节)
            for j, h in enumerate(ch_secs):
                if h[1] == "sub":
                    continue
                sec_end = ch_end
                for k in range(j + 1, len(ch_secs)):
                    if ch_secs[k][1] == "sec":
                        sec_end = ch_secs[k][0]
                        break
                ex = (ch_num, ch_title, h[2], h[3][1], None, None, h[0], None, sec_end)
                if split_level >= 3:
                    sub_entries = [sh for sh in ch_secs if sh[1] == "sub" and h[0] < sh[0] < sec_end]
                    for sj, sh in enumerate(sub_entries):
                        sub_end = sub_entries[sj + 1][0] if sj + 1 < len(sub_entries) else sec_end
                        sections.append((ch_num, ch_title, h[2], h[3][1], sh[2], sh[3][1], sh[0], None, sub_end))
                        # 节文件(除去小节) 范围截短
                        ex = (ch_num, ch_title, h[2], h[3][1], None, None, h[0], None, sub_entries[0][0])
                if ex and not (split_level >= 3 and sub_entries):
                    sections.append(ex)
                elif ex and split_level >= 3 and not sub_entries:
                    sections.append(ex)
        print(f"找到 {len(sections)} 个节")

    # ---------- 写出文件 ----------
    os.makedirs(output_dir, exist_ok=True)
    written = 0

    if split_level >= 2:
        for entry in sections:
            ch_num, ch_title, sec_num, sec_title, sub_num, sub_title, sec_start, _sec_end_v, sec_end = entry
            # 清理标题，移除章节号前缀
            clean_sec_title = clean_section_title(sec_title)
            clean_sub_title = clean_section_title(sub_title) if sub_title else None
            
            if sub_num:
                # 小节文件: {sec_num} {sub_num} {sub_title}.md
                safe_sec = sanitize(clean_sec_title)
                safe_sub = sanitize(clean_sub_title)
                sec_fn = f"{sec_num} {safe_sec}-{sub_num} {safe_sub}.md"
                content = "\n".join(body_lines[sec_start:sec_end])
                # 清理内容中的标题前缀
                content = clean_content_headers(content, clean_sec_title, clean_sub_title)
            else:
                safe_sec = sanitize(clean_sec_title)
                # 节文件: {sec_num} {sec_title}.md  (如 1.1 Coulomb's_Law.md)
                sec_fn = f"{sec_num} {safe_sec}.md"
                content = "\n".join(body_lines[sec_start:sec_end])
                # 清理内容中的标题前缀
                content = clean_content_headers(content, clean_sec_title)
            with open(os.path.join(output_dir, sec_fn), "w", encoding="utf-8") as f:
                f.write(content)
            written += 1
            print(f"  [节] {sec_fn} ({sec_end - sec_start} 行)")

    print(f"\n完成! 共创建 {written} 个文件于 {output_dir}")
    # 返回章节信息列表，供 pipeline 生成 index.md
    section_info = []
    if split_level >= 2:
        for entry in sections:
            ch_num, ch_title, sec_num, sec_title, sub_num, sub_title, sec_start, _sec_end_v, sec_end = entry
            # 清理标题，移除章节号前缀
            clean_sec_title = clean_section_title(sec_title)
            clean_sub_title = clean_section_title(sub_title) if sub_title else None
            
            if sub_num:
                safe_sec = sanitize(clean_sec_title)
                safe_sub = sanitize(clean_sub_title)
                fn = f"{sec_num} {safe_sec}-{sub_num} {safe_sub}.md"
                section_info.append((sec_num, clean_sec_title, fn, ch_num, ch_title))
            else:
                safe_sec = sanitize(clean_sec_title)
                fn = f"{sec_num} {safe_sec}.md"
                section_info.append((sec_num, clean_sec_title, fn, ch_num, ch_title))
    return section_info


def main():
    parser = argparse.ArgumentParser(description="按章节拆分 Markdown 文档")
    parser.add_argument("--input", required=True, help="输入 markdown 文件")
    parser.add_argument("--output-dir", required=True, help="输出目录")
    parser.add_argument("--level", type=int, default=2, help="拆分级别: 1=章, 2=章+节, 3=章+节+小节 (默认2)")
    parser.add_argument("--book", default="", help="输出文件前缀(书名), 默认取输入文件名")
    parser.add_argument("--no-skip-frontmatter", action="store_true", help="不移除开头的 frontmatter 块")
    args = parser.parse_args()

    split_document(
        args.input,
        args.output_dir,
        split_level=args.level,
        book_name=args.book,
        skip_frontmatter=not args.no_skip_frontmatter,
    )


if __name__ == "__main__":
    main()