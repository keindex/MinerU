---
name: md-pipeline
description: Markdown 全流程处理管道。从 output/ 读取 MinerU 的 PDF 识别结果（各分卷文件夹含 full.md + images/），通过预处理（合并 full.md 与 images）、分割（按章节层级拆分，输出 {sec_num} {sec_title}.md 格式节文件）、后处理（添加 title + column frontmatter 元数据）、生成 index.md 目录四步，将整理好的带元数据的章节化 Markdown 文档输出到 processed/ 文件夹。当用户发来 PDF 导出文件夹要求"整理"、"合并 Markdown"、"拆分章节"、"加元数据"、"预处理 PDF 导出结果"、"把 PDF 识别结果整理成带章节和元数据的文档"时触发。
version: 3.0.0
keywords:
  - markdown
  - merge
  - split
  - frontmatter
  - metadata
  - pipeline
  - MinerU
  - 预处理
  - 合并
  - 拆分
  - 元数据
  - 后处理
---

# Markdown Pipeline

将 MinerU 输出的 PDF 识别结果（`output/` 目录下的一系列分卷文件夹）完整处理为**带元数据的章节化 Markdown 文档**，输出到 `processed/` 目录。

**输出规范**：
- 目录结构：`processed/{书名_作者名}/index.md` + `sections/{sec_num}.{sec_title}.md` + `sections/images/`
- 文件名格式：`{阿拉伯数字.序号}.{标题}.md`（如 `1.1 Coulomb's_Law.md`）
- 元数据：仅 `title` 字段
- `index.md`：可点击跳转的目录

## 总览

```
预处理(merge)  →  分割(split)  →  后处理(frontmatter)  →  生成目录(index)  →  校验补全(人工)
  合并 full.md    按节拆分          加 title 元数据         生成 index.md       对照原始目录补漏
  + images/       节文件                         可点击跳转           删除合并文档
```

```
output/                          processed/{book}/
folderA/full.md   ──┐            ├── index.md           ← 4. 目录 (可点击跳转)
folderA/images/   ──┤            ├── sections/          ← 2+3. 拆分并加 frontmatter
folderB/full.md   ──┼─> pipeline │    ├── images/       ←    合并后的图片
folderB/images/   ──┤            │    ├── 1.1 Coulomb's_Law.md
folderC/full.md   ──┘            │    ├── 1.2 Electric_Field.md
                                 │    └── ...
                                 ← 5. 校验补全后删除 {book}.md
```

**规范约定**：

- **输入**：从 `output/` 目录读取 MinerU 的 PDF 识别集（每个分卷文件夹内含 `full.md` + `images/`）
- **输出**：整理好的文档放在 `processed/{书名}/` 目录中
- **代码**：所有代码文件一律放在 `src/process_md/` 中

## 触发条件

当用户有以下任一需求时使用本技能：

- 发来一系列 MinerU 导出的分卷文件夹（每个文件夹含 `full.md` 和 `images/`），要求处理
- "把 PDF 识别结果整理成文档" / "预处理这些 PDF 导出文件夹" / "处理 output 里的结果"
- "合并 full.md" / "合并 markdown" / "把几个分卷文件夹变成一个完整的文档"
- "拆成章节" / "拆分" / "按章节分割"
- "加上元数据" / "写 frontmatter" / "给 md 加 title"

## 目录结构

```
MinerU/
├── output/                          # 输入: MinerU 的 PDF 识别结果
│   └── Jackson_..._part1of5.../     #   分卷文件夹 (含 full.md + images/)
├── processed/                       # 输出: 整理好的文档
│   └── Jackson_经典电动力学/         #   一本书一个目录
│       ├── index.md                  #   目录 (可点击跳转章节文件)
│       └── sections/                 #   拆分后的章节文件
│           ├── images/               #   合并后的图片
│           └── 1.1 Coulomb's_Law.md  #   带 frontmatter (阿拉伯数字空格标题)
├── src/process_md/                  # 代码: 所有处理脚本
│   ├── pipeline.py                  #   一键入口
│   ├── merge_markdown.py            #   步骤1: 预处理(合并)
│   ├── split_sections.py            #   步骤2: 分割
│   └── add_frontmatter.py           #   步骤3: 后处理(frontmatter)
└── .agents/skills/md_pipeline/SKILL.md  # 本文档
```

> ⚠️ **注意**：`{book}.md`（合并后的完整文档）仅作为校验补全时的参考，确认无遗漏后**必须删除**，不保留在最终输出中。

## 使用方法

### 一键全流程（推荐）

```bash
# 自动在 output/ 下发现所有含 full.md 的文件夹（按书名分卷分组排序）
python src/process_md/pipeline.py \
    --book "电动力学导论" \
    --author "格里菲斯" \
    --out-root "processed/电动力学导论_格里菲斯"

# 或显式指定输入文件夹
python src/process_md/pipeline.py \
    --dirs "output/folderA,output/folderB,output/folderC" \
    --book "电动力学导论" \
    --author "格里菲斯" \
    --out-root "processed/电动力学导论_格里菲斯"
```

### 分步执行（可选）

三个步骤的脚本均支持独立调用。

**步骤 1 — 预处理（合并 `full.md` + `images/`）**：

```bash
python src/process_md/merge_markdown.py \
    --root "output" \
    --output "processed/{book}/{book}.md" \
    --images-dir "processed/{book}/images"
```

**步骤 2 — 分割**：

```bash
python src/process_md/split_sections.py \
    --input "processed/{book}/{book}.md" \
    --output-dir "processed/{book}/sections" \
    --level 2 \
    --book "{book}"
```

**步骤 3 — 后处理（添加 frontmatter）**：

```bash
python src/process_md/add_frontmatter.py \
    --dir "processed/{book}/sections"
```

**步骤 4 — 生成目录（`pipeline.py` 内置，通常无需单独调用）**：
```bash
# 由 pipeline.py 自动执行，生成 index.md
```

**步骤 5 — 校验补全与清理（必须人工执行）**：
```bash
# 1. 对照原始 PDF 目录/书签，核对 sections/ 下文件是否完整
# 2. 如有漏章节，从 {book}.md 中手动查找并创建补全
# 3. 确认无遗漏后，删除合并文档 {book}.md
rm "processed/{book}/{book}.md"
```

> `pipeline.py` 会自动执行步骤 1-4（合并、分割、frontmatter、生成目录），**步骤 5（校验补全、删除合并文档）需人工执行**，正常情况无需单独调用前四步。

### 参数说明 (pipeline.py)

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `--dirs` | 自动发现 | 逗号分隔的输入文件夹列表 |
| `--root` | `output` | 自动发现时的搜索根目录 |
| `--book` | 合并文件名 | 书名（如 `电动力学导论`） |
| `--out-root` | 必填 | 输出根目录（`processed/{book}`） |
| `--split-level` | `2` | 拆分级别：1=章，2=章+节，3=章+节+小节 |
| `--merged-name` | `{book}.md` | 合并后的文件名 |
| `--sections-dir` | `sections` | 拆分输出目录名 |
| `--overwrite-images` | 关闭 | 同名图片强制覆盖 |

## 实现逻辑

### 步骤 1：预处理（`merge_markdown.py`）

- 在 `output/` 下发现所有含 `full.md` 的文件夹
- 文件夹按 `partN` 分卷号排序（`part1of5` → 1）；无法识别的按名称自然排序
- 同前缀（同名书）的文件夹归组，组内按卷号排序，避免多本书混排
- 逐文件夹读取 `full.md`（UTF-8），拼接为一个完整文档
- 复制各 `images/` 到目标 `sections/images/`，重名跳过（哈希命名一般不冲突）
- 校验合并后文档引用的图片是否齐全，报告缺失图片

### 步骤 2：分割（`split_sections.py`）

- **根据 md 文件内目录识别章节结构**：扫描合并后文档的标题层级，自动识别节边界
  - 一级标题章：`# 章标题` + `## X.Y 节`（如 Jackson 经典电动力学）
  - 中文章：`## 第 X 章 章名` + `## X.Y 节`（如格里菲斯电动力学导论）
  - 罗马数字章：`## I. INTRODUCTION` + `### A. 节`
  - 节号支持阿拉伯数字（`1.2`）与罗马数字（`I.1`）前缀
  - 小节 `## X.Y.Z`（level 3 时拆分）
- **只输出节文件**，不输出章文件。文件名格式：`{sec_num} {sec_title}.md`（如 `1.1 Coulomb's_Law.md`）
- **删除**：前置部分（第一个章标题之前：封面/序/目录）、附录/索引（中英文 `附录`/`Appendix`/`Index`）、单字母噪声标题
- **标题缺失处理**：若某章标题丢失（直接从节开始），用内置章名表补全
- **文件名清洗**：特殊字符 → `_`，LaTeX 符号清理，空格统一为 `_`

### 步骤 3：后处理（`add_frontmatter.py`）

- **title**：取文件正文第一个 `# ~ ######` 标题；无标题时用文件名
- **只保留 `title` 字段**，旧 frontmatter 字段（如 `url`、`column`）被丢弃
- title 中的 `"` 转义为 `'`；LaTeX 内容完整保留；**幂等**（重复运行不变）

### 步骤 4：生成目录（`pipeline.py` 内置）

- 根据分割步骤返回的章节信息，生成 `index.md`
- 目录格式：按章分组，每节为可点击链接 `[sec_num sec_title](sections/filename.md)`

### 步骤 5：校验与补全（人工核对，必须执行）

- **对照原始 PDF 目录/书签**，逐章逐节核对 `sections/` 下生成的文件是否完整
- **如有漏章节**：必须从合并后的完整文档（`{book}.md`）中手动查找缺失内容，创建对应的节文件并补全到 `sections/`
- **不可用统一代码自动补全**——不同书籍的缺失模式不同，需人工判断
- 确认无遗漏后，**删除合并后的完整文档**（`{book}.md`，与 `index.md` 同级）

每个输出的章节文件带 frontmatter：

```yaml
---
title: "1.1.Coulomb's Law"
---
```

## 注意

1. **编码**：所有文件使用 UTF-8 读写
2. **图片路径**：图片位于 `sections/images/`，章节文件在 `sections/` 中，引用 `![](images/xxx.jpg)` 无需改动
3. **重复引用**：分卷间重复图片引用不影响结果（哈希命名去重）
4. **LaTeX**：数学公式在拆分、加元数据过程中完整保留
5. **幂等性**：frontmatter 步骤可安全重复执行，不产生重复字段
6. **层级**：`sections/` 中的 `.md` 与 `sections/images/` 在同一层级，引用路径正确
7. **页码清理**：MinerU 识别的 `full.md` 中，目录条目常带页码（如 `一些说明 30`）。`add_frontmatter.py` 提取 `title` 时可能将页码混入。处理后需检查并批量删除 `title` 末尾的数字页码（可用正则 `re.sub(r'\s+\d+$', '', title)` 清理）。

## 经验记录（2026-08-22）

- 批量处理 8 本书（场论、弹性理论、流体动力学、统计物理学 I/II、量子力学与路径积分、量子力学概论、量子力学第二卷），共 23 个分卷文件夹，全部完成 `pipeline.py` 全流程（合并→分割→frontmatter→目录）。
- `量子力学与路径积分` 的章节文件 `title` 混入了页码（如 `一些说明 30`），已用脚本批量修复（删除 `title` 末尾数字）。
- `量子力学（第二卷）` 使用 Cohen 格式（`§A`、`§B`、`§C`、`§D`），分割正常，生成 8 个节文件。
- `量子力学概论 翻译版 原书第3版` 生成 60 个节文件，部分缺失章节由 `pipeline.py` 自动补全（从合并文档提取）。
- 最终输出结构：`processed/{书名}/index.md` + `sections/*.md`（带 `title` frontmatter）+ `sections/images/`。合并文档 `{book}.md` 保留供人工校验，确认无遗漏后应删除。

## 经验记录（2026-08-22 补全缺失章节）

- **问题**：`split_sections.py` 依赖显式章标题（如 `# 第一章`、`## 第 1 章`）来识别章节边界。若 PDF 原书某章缺少章标题（如朗道《统计物理学 I》第一章 §1-§8 直接以 `## §1` 开始，无 `# 第一章`），分割器会将这些节归入前一章或忽略，导致 `sections/` 缺失文件。
- **现象**：`统计物理学 I` 缺失 §1-§8（第一章）、§101-§105（第十章）、§142-§153（第十四章），共 25 个节。
- **排查方法**：
  1. 对照原书目录/书签，列出应有的章节编号
  2. `grep -n '^## §' processed/书名/书名.md` 找出完整文档中所有 `## §N` 节的行号
  3. 与 `sections/` 现有文件对比，定位缺失区间
- **补全方法**：编写脚本从合并文档（`{book}.md`）按行号区间提取缺失节内容，按 `{sec_num} {sec_title}.md` 命名写入 `sections/`。关键点：
  - 以 `## §N 标题` 为起始行，下一个 `## §` 为结束行
  - 文件名特殊字符清洗复用 `split_sections.py` 的 `sanitize()`
  - 内容保留原标题行（含 `## §N`），后续 `add_frontmatter.py` 会自动提取 `title`
- **预防**：运行 `pipeline.py` 后，**必须**人工核对 `sections/` 文件数与原书目录是否一致（步骤 5），发现缺失立即从合并文档补全，而非修改分割器（不同书籍缺失模式不同，统一代码难覆盖）。

## 经验记录（2026-08-22 章标题正则修复）

- **问题**：`split_sections.py` 的章标题正则 `CHAPTER_RE` 和 `HASH_CHINESE_CHAPTER_RE` 要求 "第X章" 后必须有空格和标题（`\s+(.+)$`），但《流体动力学》等书籍的章标题格式不规范：
  - `# 第一章理想流体`（无空格）
  - `## 第二章`（无标题）
  - `## 第三章`（无标题）
  - `# 第五章流体中的传热`（无空格）
  - `# 第六章`（无标题）
  导致前 3 章（§1-§39）未被识别，`sections/` 缺失 39 个节文件。
- **修复**：将正则改为 `\s*(.*)$`，使空格和标题均为可选：
  - `CHAPTER_RE = re.compile(r"^#{1,2}\s+(第\s*([0-9一二三四五六七八九十]+)\s*章)\s*(.*)$")`
  - `HASH_CHINESE_CHAPTER_RE = re.compile(r"^#\s+(第\s*([0-9一二三四五六七八九十]+)\s*章)\s*(.*)$")`
- **验证**：修复后所有格式均能正确匹配，章号提取正确，标题为空时返回空字符串（后续逻辑会用 `MISSING_CHAPTER_TITLES` 或默认值补全）。
- **建议**：章标题正则应尽量宽容，兼容 "第X章 标题"、"第X章标题"、"第X章" 三种格式，避免因 PDF 识别格式差异导致章节识别失败。