---
name: md-pipeline
description: Markdown 全流程处理管道，将一系列 PDF 导出文件夹预处理为带元数据的章节化 Markdown 文档。包含三个步骤：预处理(按顺序合并 full.md + 合并 images 目录)、分割(按章节层级拆分为独立文件)、后处理(添加 title + column frontmatter 元数据)。当用户发来一系列 PDF 导出文件夹要求"合并 Markdown"、"拆分章节"、"加元数据"、"预处理"、"把几个文件夹变成一个完整的带章节和元数据的文档"时触发。
version: 2.0.0
keywords:
  - markdown
  - merge
  - split
  - frontmatter
  - metadata
  - pipeline
  - 预处理
  - 合并
  - 拆分
  - 元数据
---

# Markdown Pipeline

将用户发来的一系列文件夹（MinerU/PDF 导出结果）完整处理为**带元数据的章节化 Markdown 文档**。

本 skill 整合三个子流程为一个管道：

```
预处理(merge)  →  分割(split)  →  后处理(frontmatter)
```

```
分卷文件夹们                    完整 md           章节 md 文件们
folderA/full.md     ──┐                         ┌─> 第1章.md        ┐
folderA/images/     ──┤  ┌──────────┐           │ 1.1.节.md         │
folderB/full.md     ──┼─>│ merge    │──> IED.md ├─> 1.2.节.md        │─> 添加 frontmatter
folderB/images/     ──┤  │ 合并     │   +images/ │ ... (拆分后)      │   title+column
folderC/full.md     ──┘  └──────────┘           └─> 第2章.md        ┘
```

## 触发条件

当用户有以下任一需求时使用本技能：

- 发来一系列文件夹（每个文件夹内含 `full.md` 和 `images/`），要求合并
- "把这三个文件夹合起来" / "合并 full.md" / "合并 markdown"
- "合并并拆分" / "拆成章节" / "把 markdown 分割"
- "加上元数据" / "写 frontmatter" / "给 md 加 title 和 column"
- "预处理这些 PDF 导出文件夹" / "处理成完整的带章节的文档"

## 典型场景

用户给出一批 MinerU 导出的分卷文件夹，期望得到一个完整、分章节、带元数据的文档集：

```
Griffiths_电动力学导论_part1of3_p1-200.pdf-xxxx/full.md  + images/
Griffiths_电动力学导论_part2of3_p201-400.pdf-xxxx/full.md + images/
Griffiths_电动力学导论_part3of3_p401-554.pdf-xxxx/full.md + images/
```

期望输出：

```
IED.md                  ← 1. 合并: 三部分 full.md 按顺序合并
IED/images/             ←     images/ 合并
IED/sections/           ← 2. 分割: 按章节拆分
    ├── 1.0 矢量分析.md
    ├── 1.1.矢量代数.md      ← 3. 后处理: 每个文件带 frontmatter
    ├── 2.0 静电学.md
    └── ...
```

每个输出的章节文件带 frontmatter：

```yaml
---
title: "1.1 矢量代数"
column: 电动力学导论
---
```

## 使用方法

### 方式一：一键全流程（推荐）

```bash
python .agents/skills/md_pipeline/pipeline.py \
    --dirs "folderA,folderB,folderC" \
    --book "电动力学导论" \
    --out-root "C:/output/电动力学导论"
```

省略 `--dirs` 时自动在 `--root` 下发现所有含 `full.md` 的文件夹（按同名书籍分卷分组排序）。

### 方式二：分步执行

三个步骤也支持独立调用。

**步骤 1 — 合并（预处理）**：

```bash
python .agents/skills/md_pipeline/scripts/merge_markdown.py \
    --root "C:/Users/admin/MinerU" \
    --output IED.md \
    --images-dir images
```

**步骤 2 — 分割**：

```bash
python .agents/skills/md_pipeline/scripts/split_sections.py \
    --input IED.md \
    --output-dir IED_sections \
    --level 2 \
    --book "电动力学导论"
```

**步骤 3 — 添加元数据（后处理）**：

```bash
python .agents/skills/md_pipeline/scripts/add_frontmatter.py \
    --dir "C:/output/sections" \
    --column "电动力学导论"
```

### 参数说明 (pipeline.py)

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `--dirs` | 自动发现 | 逗号分隔的文件夹列表 |
| `--root` | `.` | 自动发现时的搜索根目录 |
| `--book` | 合并文件名 | 书名（column 字段 + 输出文件前缀） |
| `--out-root` | 必填 | 输出根目录 |
| `--split-level` | `2` | 拆分级别：1=章，2=章+节，3=章+节+小节 |
| `--merged-name` | `merged.md` | 合并后的文件名 |
| `--sections-dir` | `sections` | 拆分输出目录名 |
| `--overwrite-images` | 关闭 | 同名图片强制覆盖 |

## 实现逻辑

### 步骤 1：预处理（`merge_markdown.py`）

- 文件夹按 `partN` 分卷号排序（`part1of3` → 1）；无法识别的按名称自然排序
- 同前缀（同名书）的文件夹归组，组内按卷号排序，避免多本书混排
- 逐文件夹读取 `full.md`（UTF-8），拼接为一个完整文档
- 复制各 `images/` 到目标 `images/`，重名跳过；校验文档图片引用是否齐全

### 步骤 2：分割（`split_sections.py`）

- **自动识别章节结构**（三种模式自适应）：
  - 一级标题章：`# 章标题` + `## X.Y 节`（如 Jackson 经典电动力学）
  - 中文章：`## 第 X 章 章名` + `## X.Y 节`（如格里菲斯电动力学导论）
  - 罗马数字章：`## I. INTRODUCTION` + `### A. 节`
  - 节号支持阿拉伯数字（`1.2`）与罗马数字（`I.1`）前缀
  - 小节 `## X.Y.Z`（level 3 时拆分）
- 章文件包含章首导语、补充习题等所有内容；节文件按节边界切分
- **删除**：前置部分（第一个章标题之前：封面/序/目录）、附录/索引（中英文 `附录`/`Appendix`/`Index`）、单字母噪声标题
- **标题缺失处理**：若某章标题丢失（直接从节开始），用内置章名表补全
- **文件名清洗**：特殊字符 → `_`，LaTeX 符号清理，空格统一为 `_`

### 步骤 3：后处理（`add_frontmatter.py`）

- **title**：取文件正文第一个 `# ~ ######` 标题；无标题时用文件名
- **column**：`--column` 指定书名
- 只保留 `title` + `column` 两字段，旧 frontmatter 字段被替换/丢弃
- title 中的 `"` 转义为 `'`；LaTeX 内容完整保留；**幂等**（重复运行不变）

## 目录结构

```
md_pipeline/
├── SKILL.md                      # 本文档
├── pipeline.py                   # 一键入口: 三步全流程
└── scripts/
    ├── merge_markdown.py         # 步骤1 预处理: 合并 full.md + images
    ├── split_sections.py         # 步骤2 分割: 按章节拆分
    └── add_frontmatter.py        # 步骤3 后处理: 添加 frontmatter
```

## 注意事项

1. **编码**：所有文件使用 UTF-8 读写
2. **图片路径**：合并后文档与 `images/` 在同一层级，引用 `![](images/xxx.jpg)` 无需改动
3. **重复引用**：分卷间重复图片引用不影响结果（图片按哈希去重）
4. **LaTeX**：数学公式在拆分、加元数据过程中完整保留
5. **幂等性**：全流程中 frontmatter 步骤可安全重复执行，不产生重复字段
6. **输出层级**：`sections/` 中所有 `.md` 与 `sections/images` 若图片引用为 `images/...`，需将 `images/` 置于 `sections/` 同级（或用 `--images-dir` 指向适当位置）