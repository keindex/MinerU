---
name: index-url-replace
description: 将 processed/{book}/sections/*.md frontmatter 中的 url 字段替换到 index.md 的章节链接中。当用户要求"把 index.md 里的链接换成原文 URL"、"把章节链接替换成 url"、"把目录链接指向原文"、"替换 index.md 链接"、"把 frontmatter 的 url 塞进 index.md"时触发。
version: 1.0.0
keywords:
  - index.md
  - url
  - frontmatter
  - 链接
  - 替换
  - 知乎
  - zhuanlan
  - redirect
  - 目录
---

# Index URL Replace

把 `processed/{book}/index.md` 中指向本地 `sections/` 的章节链接，替换为对应 section 文件 frontmatter 中记录的原始 `url`，使目录条目可直接跳转到原文。

## 背景

`md_pipeline` 流程生成的 `index.md` 目录条目默认指向本地拆分文件：

```markdown
- [1.1 Preamble](sections/1.1%20Preamble.md)
```

而每个 section 文件的 frontmatter 中记录了原始来源 URL（例如知乎专栏）：

```markdown
---
title: 前言
url: https://zhuanlan.zhihu.com/p/2080735003407803367
---
```

本技能将两者对齐：把 `index.md` 里的本地链接替换为 frontmatter 中的 `url`，结果形如：

```markdown
- [1.1 Preamble](https://zhuanlan.zhihu.com/p/2080735003407803367)
```

## 目录结构

```
MinerU/
├── processed/                       # 输出: 整理好的文档
│   └── {book}/                      #   每本书一个目录
│       ├── index.md                  #   目录 (链接将被替换为 url)
│       └── sections/                 #   章节文件 (含 url frontmatter)
│           ├── 1.1 Preamble.chinese.md
│           └── ...
└── src/process_md/                  # 代码
    └── replace_index_urls.py         #   本技能对应的脚本
```

## 触发条件

当用户有以下任一需求时使用：

- "把 index.md 里的链接换成原文 URL"
- "把章节链接替换成 url"
- "把目录链接指向原文"
- "把 frontmatter 的 url 塞进 index.md"
- "替换 index.md 链接"
- 用户发来 `processed/{book}/` 目录，要求目录链接可跳转到原文

## 使用方法

### 一键处理单本书

```bash
python src/process_md/replace_index_urls.py \
    --root processed \
    --book Introduction_to_High_Energy_Physics_Perkins
```

### 处理 processed/ 下所有书籍

```bash
python src/process_md/replace_index_urls.py --root processed --all
```

### 仅预览不写入

```bash
python src/process_md/replace_index_urls.py --root processed --all --dry-run
```

## 实现逻辑

1. **构建 url 映射**：遍历 `processed/{book}/sections/*.md`，从每个文件的 YAML frontmatter（`--- ... ---`）中提取 `url` 字段，以文件基础名（去掉 `.md` 或 `.chinese.md` 后缀）为键建立映射。
2. **匹配链接**：用正则 `\[[^]]+\]\((sections/.*\.md)\)` 匹配 `index.md` 中的本地章节链接。
3. **解码路径**：链接路径中的 `%20` 等 URL 编码需先用 `urllib.parse.unquote` 解码，再与 section 文件基础名匹配（文件名可能含空格、括号、分号等特殊字符）。
4. **替换**：将匹配到的链接目标替换为对应 `url`，保留链接文本不变。
5. **幂等**：若 `index.md` 中已无 `sections/` 链接（已全部替换过），脚本跳过处理，不重复写入。

## 注意

1. **编码**：所有文件使用 UTF-8 读写。
2. **幂等性**：重复运行不会产生重复替换或破坏已替换的链接（外部 `https://` 链接不在 `sections/` 前缀匹配范围内）。
3. **缺失 url 的 section**：若某 section 文件无 `url` frontmatter，对应链接保持原样不动，脚本会报告替换总数（不含未匹配项）。
4. **index.md 中的非 sections/ 链接**（如外部参考链接）不会被影响。
5. **步骤归属**：本技能是 `md_pipeline` 流程的**后置可选步骤**，在 `index.md` 生成并人工校验补全完成后执行；不影响合并、分割、frontmatter 等主流程。

## 经验记录

- `Introduction_to_High_Energy_Physics_Perkins` 共 120 个 section 文件，其中 112 个带 `url` frontmatter，`index.md` 中 122 个链接（含 2 个重复条目）全部成功匹配并替换。
- 链接路径含 `%20` 编码（如 `sections/1.1%20Preamble.md`），需先解码再与实际文件名 `1.1 Preamble.chinese.md` 比对。
- 正则 `\[[^]]+\]\((sections/.*\.md)\)` 中 `.*` 默认非贪婪，但因一行只有一个链接且目标以 `.md` 结尾，可安全匹配含括号的文件名（如 `9.2 Grand_unified_theories_the_SU(5)_GUT.md`）。