#!/usr/bin/env python3
"""
知乎批量查询使用示例
从配置文件读取参数并执行查询
"""

import json
import sys
from pathlib import Path

# 添加当前目录到路径
sys.path.insert(0, str(Path(__file__).parent))

from zhihu_batch_query import ZhihuBatchQuery


def load_config(config_path: str = "zhihu_config.json") -> dict:
    """加载配置文件"""
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"配置文件不存在: {config_path}")
        print("请先复制 zhihu_config.json.example 并填入你的认证信息")
        return {}
    except json.JSONDecodeError as e:
        print(f"配置文件格式错误: {e}")
        return {}


def main():
    # 加载配置
    config = load_config()
    if not config:
        return
    
    zhihu_config = config.get('zhihu', {})
    
    # 检查必要参数
    cookie = zhihu_config.get('cookie', '').strip()
    if not cookie:
        print("错误: 配置文件中 cookie 为空")
        print("请编辑 zhihu_config.json 填入你的 cookie")
        return
    
    # 创建查询器
    query = ZhihuBatchQuery(
        user_id=zhihu_config.get('user_id', 'yjk-59-34'),
        limit=zhihu_config.get('limit', 20),
        delay=zhihu_config.get('delay', 1.0)
    )
    
    # 设置认证信息
    query.set_cookie(cookie)
    
    x_zse_96 = zhihu_config.get('x_zse_96', '').strip()
    x_zst_81 = zhihu_config.get('x_zst_81', '').strip()
    
    if x_zse_96:
        query.set_signature(x_zse_96=x_zse_96)
    if x_zst_81:
        query.set_signature(x_zst_81=x_zst_81)
    
    # 执行查询
    output_file = zhihu_config.get('output_file', 'zhihu_articles.json')
    max_pages = zhihu_config.get('max_pages', 0)
    
    articles = query.query_all(
        max_pages=max_pages,
        output_file=output_file
    )
    
    # 显示摘要
    query.print_summary(articles)


if __name__ == '__main__':
    main()