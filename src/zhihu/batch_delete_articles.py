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
    'cookie': 'q_c1=50e987aacced4cd29d23bf42476df39c|1786959087000|1786959087000;z_c0=2|1:0|10:1787302741|4:z_c0|92:Mi4xcEtMU05RQUFBQUFHODFkVjBMaV9IQ1lBQUFCZ0FsVk5VMkYxYXdDVDNLM2hPQ05DeXl4N29TNWVjMWJrZkxEYkNR|0c524b788cd92c8f5318a472b8831cba813c1bfe10f619838cdc1d22fd694790;osd=UVkQBE6uG--YTH-TRizrOnf_hCxaykuC7Q8OwhXSbYryPDTmDRBpffZIeZVGdtPJTJt-ROKjFFiTgaS_aQ4qxjQ=;Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1787983032;HMACCOUNT=F4A2E54A8E7E8BA6;gdxidpyhxdE=Ex9HQZtXoorUpl1Vb1O9223bEbv7N20KZkpHNdIJL3XBZANBxJNgjqtB%5CXOHRBfVcw%2FRIcmyJxU%2BXGsxq61vGUBR2PYHi0YhVtdZnazLxCi%5CelTil%2BDZWeqwihSjcsTVpo5Z4Cv9lozNLDDMSlmyqS7Ay%2FKmk8DIBJ1tKX9Gb9031Dq2%3A1787303514084;_xsrf=ifVvCefqIn8Ck4Y18lji0R2lXRtBDAKd;BEC=32377ec81629ec05d48c98f32428ae46;captcha_session_v2=2|1:0|10:1787302607|18:captcha_session_v2|88:YUFIbnJuY0RoUHNwR3Fqd0FhaHU4S0lFVkpzV2FpdHNsN2w0T2Z5dVM3ZklUTGtiK1ZORW8rVDNQdTlibCtjeA==|df11923bf9cf267160bd64b359ab21799dc4a64f6e704051f5641f8c888363f8;JOID=VVgWC06qGumXTHuSQCPrPnb5iyxey02N7QsPxBrSaYv0MzTiDBZmffJJf5pGctLPQ5t6ReSsFFySh6u_bQ8syTQ=;__snaker__id=l8y6yOlWSBc4Hq3V;__zse_ck=005_Qsg6fNyH9kKeytKWhoMH5iQnYXibaNDyTXWus36sDjvLNLFQVhMibi9oFlnIJTbz4fdjxuSsqn0krgLvfZLqOe24m36KRQVzEOZ93XbZyrLZ6Lpc9ANd6YvHbvoli91b-QfyfPhpOQbhMWQf6rCMejwUdt4PiMuoF61HhOKU+zsnxr6jee9v/fB2syUQbZlkv6Vm5jCzGowRAcxUtTlov4TKn+Xf7cXroYiB2g3foMaAobzdB11kCGKOSgSfYSMK8;_zap=029ea90a-ebe6-43fb-903b-c644b08b9914;d_c0=BvNXVdC4vxyPTlM_l0RTnvop14BLqRzv15w=|1786682578;Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1787502375,1787515624,1787889300,1787983032;SESSIONID=fTowEsUQztahrMwO32B7dL65BytbLak2qRm3gLYHxMn'
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