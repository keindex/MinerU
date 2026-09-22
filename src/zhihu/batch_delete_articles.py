#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
批量删除知乎文章脚本
从 zhihu_articles.json 读取所有文章 ID 并调用删除 API
"""

import json
import time
import requests

# 请求头（需要替换为你的有效 cookie 和 token）
headers = {
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua': '"Not=A?Brand";v="99", "Google Chrome";v="151", "Chromium";v="151"',
    'x-zse-96': '2.0_7ittm16eYkWdxCAAlQ/TD8xoRgRtvMgbVUuvgucX/BDUa7xwBqFHapDzLH1koFXe',
    'sec-ch-ua-mobile': '?0',
    'x-requested-with': 'fetch',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36',
    'x-zst-81': '3_2.0aR_sn77yn6O92wOB8hPZnQr0EMYxc4f18wNBUgpTQ6nxERFZmLY0-4Lm-h3_tufIwJS8gcxTgJS_AuPZNcXCTwxI78YxEM20s4PGDwN8gGcYAupMWufIeQuK7AFpS6O1vukyQ_R0rRnsyukMGvxBEqeCiRnxEL2ZZrxmDucmqhPXnXFMTAoTF6RhRuLPFHF0quFmobXC28X9HqN_792MWCSm6M3L3JxGTvX9rBH8zqcppBc9sHgMSDrTvRYxTwoMsqYf6Xx0bMt8tq2mRwH9_9xGcGYsZuVfpTSGODU_ICLGPCHmuGCf6Q9MA921oCLy49LmJXSfbutsWrHMfLCyfqxYkBVsNwVLFUxf6i9_CCexOqfzdGYMSACO9qYpSR2qThC_ZbxMJLO8VwOOy9p1NJVZPGe1tuVZ4BoYXhS_hh3YuGoLf_cGEJV1nqe8qBe_GrSVkXOMbXcKkGX1kwL_zbL1eTYYQXXC1QNC',
    'x-zse-93': '101_3_3.0',
    'x-xsrftoken': 'ifVvCefqIn8Ck4Y18lji0R2lXRtBDAKd',
    'accept': '*/*',
    'origin': 'https://www.zhihu.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.zhihu.com/people/yjk-59-34/posts',
    'accept-encoding': 'gzip, deflate, br, zstd',
    'accept-language': 'zh-CN,zh;q=0.9',
    'priority': 'u=1, i',
    'cookie': "z_c0=2|1:0|10:1788511705|4:z_c0|92:Mi4xcEtMU05RQUFBQUJGeFJrNExyclRIQ1lBQUFCZ0FsVk4yZE9IYXdCdHRJVE1nZFB2SmFmUWNfWUU4VjdPZEQ3N1FR|2600bffb992bdbf5780fd9b143b7c70868a22da84a3727143bf0261f0368a3cb;__zse_ck=005_4vIbXwufkAfY8ETDMKXkyV8YJoi8Ec5G9anErLOg1vA/pt=SWXXnnqWxglFIxhVARpgXlvBJkAElwDbJsPA19LgsETV0RtfxShiGRFt8Wqd2D=BqYW4PEFK1pfwUdg9K-3aPXnKVpYr0DVQtKUzKBTHAx2ZPVLkL04qXbiNE3datF5DRFVCZzXUqsQq1IviMVAaY/Bl5Hytj8u+oxnbOVaZx7Bb/lIHJSdf/HRH97UhhsZ+6R7jSFhISqM3lV/L+p",
    }

def load_article_ids(json_file):
    """从 JSON 文件加载所有文章 ID"""
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return [article['id'] for article in data['articles']]

def delete_article(article_id, headers, delay=1.0):
    """删除单篇文章"""
    url = f"https://www.zhihu.com/api/v4/articles/{article_id}"
    try:
        response = requests.request("DELETE", url, headers=headers, data=None)
        return response.status_code, response.text
    except Exception as e:
        return None, str(e)

def main():
    # 加载文章 ID
    article_ids = load_article_ids('zhihu_articles.json')
    print(f"共发现 {len(article_ids)} 篇文章待删除")
    
    # 统计结果
    success = 0
    failed = 0
    errors = []
    
    for i, article_id in enumerate(article_ids, 1):
        print(f"[{i}/{len(article_ids)}] 正在删除文章 {article_id}...", end=" ")
        
        status_code, response_text = delete_article(article_id, headers)
        
        if status_code == 200 or status_code == 204:
            print(f"✓ 成功 (状态码: {status_code})")
            success += 1
        else:
            print(f"✗ 失败 (状态码: {status_code}, 响应: {response_text[:100]})")
            failed += 1
            errors.append((article_id, status_code, response_text))
        
        # 避免请求过快被限流
        if i < len(article_ids):
            time.sleep(1.5)
    
    # 输出统计结果
    print("\n" + "=" * 50)
    print(f"删除完成!")
    print(f"成功: {success}")
    print(f"失败: {failed}")
    
    if errors:
        print("\n失败详情:")
        for article_id, status, resp in errors:
            print(f"  {article_id}: 状态码={status}, 响应={resp[:200]}")

if __name__ == "__main__":
    main()