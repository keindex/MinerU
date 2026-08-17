# Markdown Document Section Splitter (已整合)

> ⚠️ 本 skill 已与 `markdown-preprocess` 整合为 **`md_pipeline`**（预处理+分割+后处理一键完成）。
>
> 拆分功能已泛化为：`md_pipeline/scripts/split_sections.py`
>
> ```bash
> python .agents/skills/md_pipeline/scripts/split_sections.py \
>     --input <合并后的.md> --output-dir <sections目录> --level 2 --book "书名"
> ```
>
> 完整流程（合并→拆分→元数据）请使用：
>
> ```bash
> python .agents/skills/md_pipeline/pipeline.py --dirs "folderA,folderB" --book "书名" --out-root "输出"
> ```

## 功能说明

输入一篇长篇 markdown 文档，先根据用户提供的文档目录找出正确的章节层级结构；
然后询问用户要拆分到第几级；
然后按照目录提供的每一章的标题，去文章中搜索标题找到对应的拆分点；
然后按照这种方法，把每一章节的都拆分出来。

## 使用方法

```
当用户要求拆分 Markdown 文件的时候触发
```

### 判断示例
现在需要拆分文章`thesis1.md`：
```markdown
## I. INTRODUCTION      
Content of Introduction        
### 1.1 Background     
Content of echo ground      
## II. METHOD                 
... 
```
如果用户拆分到第 1 级，则根据搜索发现
`## I. INTRODUCTION   `为一个拆分点
`## II. METHOD   `为一个拆分点
输出：
thesis1 I.INTRODUCTION.md
```markdown
## I. INTRODUCTION      
Content of Introduction        
### 1.1 Background     
Content of echo ground      
```
thesis1 II.METHOD.md
```markdown
## II. METHOD
···
```
如果用户拆分到第 2 级，则根据搜索发现
`## I. INTRODUCTION   `为一个拆分点
`### 1.1 Background` 为一个拆分点
`## II. METHOD   `为一个拆分点
输出：
thesis1 I.INTRODUCTION.md
```markdown
## I. INTRODUCTION
Content of Introduction
```
thesis1 I.INTRODUCTION-1.1.Background.md
```markdown
### 1.1 Background
Content of echo ground
```
thesis1 II.METHOD.md
```markdown
## II. METHOD
···
```


## 输出文件命名规则

**格式**：`原文档名 章节标识符.章节标题-子章节标识符.子章节标题.md`

**文件名清洗规则**：
- 特殊字符（`/`、`\`、`:`、`*`、`?`、`"`、`<`、`>`、`|`）替换为 `_`


## 需要删除的内容

1. **作者信息**：文档开头的作者列表、机构信息、Dated 等
2. **关键词**：Abstract 中的 PACS numbers 等
3. **致谢**：ACKNOWLEDGMENTS 章节
4. **附录**：所有 Appendix 章节（Appendix A, Appendix B, Appendix D 等）
5. **乱码**：移除任何无法正常显示的字符或乱码文本

## 保留的文档结构

```markdown
# 文件名：full.III.RESULTS_AND_DISCUSSIONS.md

## 未拆分的子章节/标题

正文
```

## 注意事项

1. **编码**：所有文件使用 UTF-8 编码读取和写入
2. **路径**：输出目录自动创建
3. **图片**：图片引用路径保持相对路径不变
4. **LaTeX**：数学公式（如 `$K_{\tau,\nu}$`）保持完整


