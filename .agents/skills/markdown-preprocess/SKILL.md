---
name: markdown-preprocess
description: "[已合并至 md_pipeline] Markdown 预处理工具：合并 full.md + images。本 skill 已与分割、元数据后处理整合为统一管道 md_pipeline，请优先使用 md_pipeline。保留本目录仅作兼容入口。当用户发来一系列 PDF 导出文件夹并要求"合并 Markdown"、"合并 full.md"、"预处理"、"把 images 合并"、"将这几个文件夹合并成一个文件"时，应引导至 md_pipeline 技能。"
version: 2.0.0
keywords:
  - markdown
  - merge
  - full.md
  - images
  - preprocess
  - 预处理
  - 合并
  - pipeline
---

# Markdown Preprocess (已整合)

> ⚠️ 本 skill 已与 `markdown-section-splitter` 整合为 **`md_pipeline`**（预处理+分割+后处理一键完成）。
>
> 如需完整流程（合并→拆分→元数据），请使用：
>
> ```bash
> python .agents/skills/md_pipeline/pipeline.py --dirs "folderA,folderB" --book "书名" --out-root "输出目录"
> ```
>
> 本目录仅保留预处理（合并）脚本，供独立调用。

# Markdown Preprocess

将用户发来的一系列文件夹（MinerU/PDF 导出结果）预处理为单个 Markdown 文档：

1. **按顺序合并 `full.md`** — 各部分按分卷顺序拼接为一个完整的 `.md` 文件
2. **合并 `images/`** — 将各文件夹下的 `images` 目录全部复制到目标 `images/` 目录
3. **校验图片引用** — 检查合并后的文档中引用的图片是否齐全
4. **添加 frontmatter** — 为所有 Markdown 文件写入 `title` + `column` 元数据

## 触发条件

当用户有以下任一需求时使用本技能：

- 发来一系列文件夹（每个文件夹内含 `full.md` 和 `images/`），要求合并
- "把这三个文件夹合起来"
- "合并 full.md" / "合并 markdown"
- "把 images 文件夹合并 / 汇总"
- "预处理这些 PDF 导出文件夹"
- "加上元数据" / "写 frontmatter" / "给 md 加 title 和 column"

## 典型场景

用户给出一批 MinerU 导出的分卷文件夹，例如：

```
Griffiths_电动力学导论_part1of3_p1-200.pdf-xxxx/full.md  + images/
Griffiths_电动力学导论_part2of3_p201-400.pdf-xxxx/full.md + images/
Griffiths_电动力学导论_part3of3_p401-554.pdf-xxxx/full.md + images/
```

期望得到：

```
IED.md                    ← 三部分 full.md 按顺序合并
IED_sections/images/      ← 三部分 images/ 合并 (或者用户指定目录)
```

## 使用方法

### 方式一：自动发现（推荐）

在含各分卷文件夹的根目录下运行，自动识别所有含 `full.md` 的文件夹并按 `partN` 顺序排序：

```bash
python .agents/skills/markdown-preprocess/merge_markdown.py \
    --root "C:/Users/admin/MinerU" \
    --output IED.md \
    --images-dir IED_sections/images
```

### 方式二：显式指定文件夹列表

```bash
python .agents/skills/markdown-preprocess/merge_markdown.py \
    --dirs "folderA,folderB,folderC" \
    --output merged.md \
    --images-dir images
```

### 方式三：后处理 — 添加 frontmatter 元数据

为目录下所有 `.md` 文件添加 `title` + `column` 两个字段的 frontmatter：

```bash
python .agents/skills/markdown-preprocess/add_frontmatter.py \
    --dir "C:/Users/admin/MinerU/IED_sections" \
    --column "电动力学导论"
```

### 参数说明

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `--dirs` | 自动发现 | 逗号分隔的文件夹列表 |
| `--output` | `merged.md` | 合并后的 Markdown 输出文件名 |
| `--images-dir` | `images` | 图片输出目录（相对输出文件所在位置） |
| `--root` | `.` | 自动发现时的搜索根目录 |
| `--overwrite` | 关闭 | 同名图片强制覆盖（默认跳过） |

## 实现逻辑

### 1. 文件夹顺序

- 优先识别文件夹名中的分卷号：`part1of3` → 1，`part2of3` → 2，按数字升序
- 无法识别的文件夹按名称**自然排序**（`part10` 排在 `part2` 之后）

### 2. Markdown 合并

- 逐文件夹读取 `full.md`（UTF-8），以换行符 `\n` 拼接
- 保持各部分内容的相对路径图片引用格式 `![](images/xxx.jpg)` 不变

### 3. 图片合并

- 复制各文件夹 `images/` 下所有文件到目标 `images/` 目录
- 若目标已存在同名文件（哈希命名一般不会冲突），默认跳过，不覆盖

### 4. 校验

- 扫描合并后文档中的图片引用 `![...](images/xxx.jpg)`
- 报告缺失的图片文件，便于及时发现分卷缺图

### 5. frontmatter 元数据 (`add_frontmatter.py`)

- **title**：取文件正文第一个 `# ~ ######` 标题；无标题时回退到文件名
- **column**：由 `--column` 参数指定的书名
- 输出格式：

```yaml
---
title: "1.1 矢量代数"
column: 电动力学导论
---
```

- 已有 frontmatter 的旧字段会被**替换/丢弃**，最终只保留这两字段
- title 中的 `"` 会转义为 `'`，避免破坏 YAML；LaTeX 内容（如 `$^{12}$`）完整保留
- **幂等**：对已处理过的文件重复运行不会产生变化

## 注意事项

1. **编码**：所有文件使用 UTF-8 读写
2. **图片路径**：合并后若文档与 `images/` 在同一层级（如 `IED.md` 与 `images/` 平级），引用无需改动；若输出到其他层级，需相应调整路径
3. **重复引用**：分卷文件间若有重复图片引用，不影响合并结果（图片按哈希去重）
4. **脚本**：`merge_markdown.py`（合并）与 `add_frontmatter.py`（元数据）均可直接复制到项目根目录使用，也支持作为模块 `from merge_markdown import merge_markdown` 调用