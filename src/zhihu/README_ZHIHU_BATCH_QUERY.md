# 知乎文章批量查询脚本

支持分页查询知乎用户的所有文章，自动处理 offset 循环请求直到结束。

## 文件说明

| 文件 | 说明 |
|------|------|
| `zhihu_batch_query.py` | 核心查询类，支持命令行参数 |
| `run_batch_query.py` | 从配置文件读取参数执行查询 |
| `zhihu_config.json` | 配置文件模板 |

## 使用方法

### 1. 获取认证信息

在浏览器中打开知乎个人主页，打开开发者工具 (F12) -> Network 面板：
1. 访问 `https://www.zhihu.com/people/你的用户ID`
2. 在 Network 中找到 `activities?limit=...` 请求
3. 复制 Request Headers 中的：
   - `cookie`
   - `x-zse-96` (如果有)
   - `x-zst-81` (如果有)

### 2. 配置认证信息

编辑 `zhihu_config.json`：

```json
{
  "zhihu": {
    "user_id": "yjk-59-34",
    "cookie": "你的cookie字符串",
    "x_zse_96": "2.0_xxx...",
    "x_zst_81": "3_2.0xxx...",
    "limit": 20,
    "delay": 1.0,
    "max_pages": 0,
    "output_file": "zhihu_articles.json"
  }
}
```

### 3. 运行查询

```bash
# 使用配置文件运行
python run_batch_query.py

# 或直接使用命令行参数
python zhihu_batch_query.py --cookie "你的cookie" --x-zse-96 "签名" --output articles.json --summary
```

## 参数说明

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `--user-id` | 知乎用户ID | yjk-59-34 |
| `--limit` | 每页数量 | 20 |
| `--delay` | 请求间隔(秒) | 1.0 |
| `--max-pages` | 最大页数(0=无限制) | 0 |
| `--output` | 输出文件路径 | - |
| `--cookie` | Cookie字符串 | 必填 |
| `--x-zse-96` | x-zse-96签名 | 可选 |
| `--x-zst-81` | x-zst-81签名 | 可选 |
| `--summary` | 显示文章摘要 | False |

## 输出格式

结果保存为 JSON 格式：

```json
{
  "user_id": "yjk-59-34",
  "total_count": 150,
  "articles": [
    {
      "id": "123456789",
      "title": "文章标题",
      "url": "https://zhuanlan.zhihu.com/p/123456789",
      "excerpt": "文章摘要...",
      "created_time": 1699999999,
      "updated_time": 1699999999,
      "voteup_count": 100,
      "comment_count": 20,
      "author": "作者名",
      "raw_data": {...}
    }
  ]
}
```

## 注意事项

1. **频率限制**: 建议 `delay` 设置为 1-2 秒，避免被封 IP
2. **签名失效**: `x-zse-96` 和 `x-zst-81` 有时效性，失效时需重新获取
3. **Cookie 过期**: Cookie 定期过期，需定期更新
4. **数据量大**: 文章很多时建议分批次查询，使用 `--max-pages` 限制

## 常见问题

### Q: 返回 403 Forbidden
A: Cookie 或签名失效，请重新从浏览器获取

### Q: 只能获取第一页
A: 检查 `x-zse-96` 和 `x-zst-81` 是否正确，翻页请求需要正确的签名

### Q: 获取到的文章数量不对
A: 知乎活动流包含回答、想法等类型，脚本已筛选 `type == 'article'` 的内容