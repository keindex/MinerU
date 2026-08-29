#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
从指定文件夹的所有 .md 文件中读取 frontmatter 的 url 字段，
删除对应的知乎文章，并移除 md 文件中的 url 字段。

用法:
  python delete_zhihu_articles_from_md.py --dir "archive" --cookie "your_cookie_here"
  python delete_zhihu_articles_from_md.py --dir "archive" --cookie "__snaker__id=koY9onIpDEVj3jFh;gdxidpyhxdE=468uZdblkrxVybDVgCzZW6XtPxEkIvz1XOWEfE7QCs801fd6lsBzGH7%2FUBm3NZNV%2FSCEOqd45mYp%5C6ULEkvODodMwZb8MRcMvtToTLxIjPQ9TzJLcAGxHRj8snqTEVspqee0Vv%5CQ7c%2FP%2B4PVu%2F%2Fbbjt3aCQeC7WhkZ%5CAGV9sX85fRcJR%3A1786557454806;SESSIONID=sYf2puAQ248dMH02kruAHQGbNn2NMNmOmBLXxxuX9YQ;osd=VV4VBEK1CSTXUKYIQjPy8D_qWbxflywA-n2ELWaYKwHzfYsqZyQOvL1foQlLT7hyRrUvLopptsq1U6oFHufH3Gk=;z_c0=2|1:0|10:1787302741|4:z_c0|92:Mi4xcEtMU05RQUFBQUFHODFkVjBMaV9IQ1lBQUFCZ0FsVk5VMkYxYXdDVDNLM2hPQ05DeXl4N29TNWVjMWJrZkxEYkNR|0c524b788cd92c8f5318a472b8831cba813c1bfe10f619838cdc1d22fd694790;Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1787889302;HMACCOUNT=F4A2E54A8E7E8BA6;_xsrf=ifVvCefqIn8Ck4Y18lji0R2lXRtBDAKd;captcha_session_v2=2|1:0|10:1787302607|18:captcha_session_v2|88:YUFIbnJuY0RoUHNwR3Fqd0FhaHU4S0lFVkpzV2FpdHNsN2w0T2Z5dVM3ZklUTGtiK1ZORW8rVDNQdTlibCtjeA==|df11923bf9cf267160bd64b359ab21799dc4a64f6e704051f5641f8c888363f8;__zse_ck=005_Qsg6fNyH9kKeytKWhoMH5iQnYXibaNDyTXWus36sDjvLNLFQVhMibi9oFlnIJTbz4fdjxuSsqn0krgLvfZLqOe24m36KRQVzEOZ93XbZyrLZ6Lpc9ANd6YvHbvoli91b-QfyfPhpOQbhMWQf6rCMejwUdt4PiMuoF61HhOKU+zsnxr6jee9v/fB2syUQbZlkv6Vm5jCzGowRAcxUtTlov4TKn+Xf7cXroYiB2g3foMaAobzdB11kCGKOSgSfYSMK8;_zap=029ea90a-ebe6-43fb-903b-c644b08b9914;BEC=4589376d83fd47c9203681b16177ae43;d_c0=BvNXVdC4vxyPTlM_l0RTnvop14BLqRzv15w=|1786682578;Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1787226400,1787502375,1787515624,1787889300;Hm_lvt_bff3d83079cef1ed8fc5e3f4579ec3b3=1786186026,1786354693,1786554693,1787226486;JOID=UVgUAkmxDyXRW6IOQzX59DnrX7dbkS0G8XmCLGCTLwfye4AuYSUIt7lZoA9AS75zQL4rKItvvc6zUqwOGuHG2mI=" --workers 5 --delay 0.5

  """

import os
import re
import json
import time
import argparse
import requests
import concurrent.futures
from pathlib import Path


# 请求头模板（需要替换 cookie）
DEFAULT_HEADERS = {
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua': '"Not=A?Brand";v="99", "Google Chrome";v="151", "Chromium";v="151"',
    'x-zse-96': '2.0_bDw+J3URW0rwbyNRg5q=Ut/FKPtBmYkWQguRxWIJX/6AudsGl/D1GGe3sFkVc3m2',
    'sec-ch-ua-mobile': '?0',
    'x-requested-with': 'fetch',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36',
    'x-zst-81': '3_2.0aR_sn77yn6O92wOB8hPZnQr0EMYxc4f18wNBUgpTQ6nxERFZmLY0-4Lm-h3_tufIwJS8gcxTgJS_AuPZNcXCTwxI78YxEM20s4PGDwN8gGcYAupMWufIeQuK7AFpS6O1vukyQ_R0rRnsyukMGvxBEqeCiRnxEL2ZZrxmDucmqhPXnXFMTAoTF6RhRuLPF7YLPhxKqrS86CXKfw3_1GXCPgOf-BVVNq38gg2BnbcGuJSKx9tYfgO8AheTvRYxTwoMsqYf6Xx0bMt8tq2mRwH9_9xGcGYsZuVfpTSGODU_ICLGPCHmuGCf6Q9MA921oCLy49LmJXSfbutsWrHMfLCyfqxYkBVsNwVLFUxf6i9_CCexOqfzGUXfevOGkiLVSX208Dc_Qiu9thHBb_pMlGwY-vSYUBtmWhef2Bx9uuLCVucsSTo11MpKzbg9XrS_rgH0GrS1qbxyOUFYeAX1cGHBQGSma9HpwwXCBwYC',
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
}


def extract_article_id_from_url(url: str) -> str:
    """从知乎文章 URL 中提取文章 ID"""
    # 匹配 https://zhuanlan.zhihu.com/p/1234567890 或类似格式
    match = re.search(r'zhuanlan\.zhihu\.com/p/(\d+)', url)
    if match:
        return match.group(1)
    # 备选：直接匹配数字 ID
    match = re.search(r'/(\d{18,})', url)
    if match:
        return match.group(1)
    return None


def parse_frontmatter(content: str):
    """解析 frontmatter，返回 (frontmatter_dict, body_content)"""
    match = re.match(r'^---\n(.*?)\n---\s*\n?', content, re.DOTALL)
    if not match:
        return {}, content
    
    frontmatter_text = match.group(1)
    body = content[match.end():]
    
    # 简单的 YAML 解析（只处理 key: value 格式）
    frontmatter = {}
    for line in frontmatter_text.split('\n'):
        line = line.strip()
        if ':' in line:
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip().strip('"\'')
            frontmatter[key] = value
    
    return frontmatter, body


def build_frontmatter(frontmatter: dict) -> str:
    """构建 frontmatter 字符串"""
    if not frontmatter:
        return ""
    
    lines = ["---"]
    for key, value in frontmatter.items():
        # 转义引号
        safe_value = str(value).replace('"', '\\"')
        lines.append(f'{key}: "{safe_value}"')
    lines.append("---")
    lines.append("")  # 空行
    return "\n".join(lines)


def prepare_file(file_path: Path, headers: dict) -> tuple:
    """预解析文件：提取 url 和 article_id，返回 (file_path, result_dict)"""
    result = {
        'file': str(file_path),
        'rel_path': str(file_path.relative_to(file_path.anchor)),
        'success': False,
        'article_id': None,
        'url': None,
        'deleted': False,
        'error': None
    }
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        result['error'] = f"读取文件失败: {e}"
        return file_path, result

    frontmatter, body = parse_frontmatter(content)
    url = frontmatter.get('url')
    if not url:
        result['error'] = "无 url 字段"
        return file_path, result
    result['url'] = url

    article_id = extract_article_id_from_url(url)
    if not article_id:
        result['error'] = f"无法从 URL 提取文章 ID: {url}"
        return file_path, result
    result['article_id'] = article_id
    result['frontmatter'] = frontmatter
    result['body'] = body
    return file_path, result


def delete_article(article_id: str, cookie: str, xsrf_token: str) -> tuple:
    """删除单篇知乎文章"""
    url = f"https://www.zhihu.com/api/v4/articles/{article_id}"
    hdrs = DEFAULT_HEADERS.copy()
    hdrs['cookie'] = cookie
    hdrs['x-xsrftoken'] = xsrf_token
    try:
        response = requests.request("DELETE", url, headers=hdrs, data=None, timeout=30)
        return response.status_code, response.text
    except Exception as e:
        return None, str(e)


def process_with_delay(args_tuple, cookie: str, xsrf: str, delay: float) -> dict:
    """带延迟的单文件处理函数（含删除 API 调用 + 写回文件）"""
    file_path, prep_result = args_tuple

    if prep_result['error']:
        return prep_result

    article_id = prep_result['article_id']

    # 删除文章
    url = f"https://www.zhihu.com/api/v4/articles/{article_id}"
    hdrs = DEFAULT_HEADERS.copy()
    hdrs['cookie'] = cookie
    hdrs['x-xsrftoken'] = xsrf
    try:
        response = requests.request("DELETE", url, headers=hdrs, data=None, timeout=30)
        status_code, response_text = response.status_code, response.text
    except Exception as e:
        status_code, response_text = None, str(e)

    if status_code in (200, 204):
        prep_result['deleted'] = True
        prep_result['success'] = True
        # 移除 url 字段并写回文件
        if 'url' in prep_result['frontmatter']:
            del prep_result['frontmatter']['url']
        new_content = build_frontmatter(prep_result['frontmatter']) + prep_result['body'].lstrip('\n')
        try:
            with open(file_path, 'w', encoding='utf-8', newline='\n') as f:
                f.write(new_content)
        except Exception as e:
            prep_result['error'] = f"写入文件失败: {e}"
            prep_result['success'] = False
    elif status_code == 404 or '资源不存在' in response_text or '4041' in response_text:
        # 文章已不存在（可能已被删除），视为成功处理，仍需移除 url 字段
        prep_result['deleted'] = True
        prep_result['success'] = True
        prep_result['error'] = None
        if 'url' in prep_result['frontmatter']:
            del prep_result['frontmatter']['url']
        new_content = build_frontmatter(prep_result['frontmatter']) + prep_result['body'].lstrip('\n')
        try:
            with open(file_path, 'w', encoding='utf-8', newline='\n') as f:
                f.write(new_content)
        except Exception as e:
            prep_result['error'] = f"写入文件失败: {e}"
            prep_result['success'] = False
    else:
        prep_result['error'] = f"删除失败: 状态码={status_code}, 响应={response_text[:200]}"

    return prep_result


def main():
    import sys, io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    import threading
    parser = argparse.ArgumentParser(description="从 md 文件的 frontmatter 中读取 url，删除知乎文章并移除 url 字段")
    parser.add_argument("--dir", required=True, help="包含 .md 文件的目录（递归处理）")
    parser.add_argument("--cookie", required=True, help="知乎 Cookie 字符串")
    parser.add_argument("--delay", type=float, default=1.5, help="API 请求间隔（秒），默认 1.5")
    parser.add_argument("--workers", type=int, default=5, help="并发线程数，默认 5")
    parser.add_argument("--dry-run", action="store_true", help="试运行，不实际删除文章和修改文件")
    parser.add_argument("--pattern", default="*.md", help="文件匹配模式，默认 *.md")
    args = parser.parse_args()

    target_dir = Path(args.dir)
    if not target_dir.exists():
        print(f"目录不存在: {target_dir}")
        return

    xsrf = args.cookie.split('_xsrf=')[1].split(';')[0] if '_xsrf=' in args.cookie else 'ifVvCefqIn8Ck4Y18lji0R2lXRtBDAKd'

    md_files = sorted(target_dir.rglob(args.pattern))
    total = len(md_files)
    print(f"发现 {total} 个 .md 文件，并发数: {args.workers}，间隔: {args.delay}s")

    if args.dry_run:
        print("=== 试运行模式，不实际删除 ===")

    lock = threading.Lock()
    fail_count = [0]
    success_count = [0]

    # 阶段 1: 预解析所有文件（提取 url/article_id）
    pre_results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as executor:
        for future in concurrent.futures.as_completed(
            {executor.submit(prepare_file, f, {}): f for f in md_files}
        ):
            _, result = future.result()
            pre_results.append(result)

    for i, result in enumerate(pre_results, 1):
        rel = Path(result['file']).relative_to(target_dir)
        if result['error'] == "无 url 字段":
            print(f"[{i}/{total}] {rel}  -> 跳过（无 url）")
        elif result['error']:
            print(f"[{i}/{total}] {rel}  -> 错误: {result['error']}")
            fail_count[0] += 1
        else:
            print(f"[{i}/{total}] {rel}  -> 文章 ID: {result['article_id']}")
            success_count[0] += 1

    if args.dry_run:
        print("\n=== 试运行结束，未执行任何删除操作 ===")
        return

    # 阶段 2: 按起始时间差调度并发删除
    task_args = [(Path(r['file']), r) for r in pre_results if r['article_id'] is not None]
    stagger = args.delay / args.workers  # 每个任务错开的起始时间（秒）
    deleted_ids = set()  # 记录已成功删除的文章 ID，避免 404 误报失败

    print(f"\n开始并发删除（起始间隔 {stagger:.2f}s），请稍候...")
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = []
        for i, (fp, r) in enumerate(task_args):
            future = executor.submit(process_with_delay, (fp, r), args.cookie, xsrf, args.delay)
            if i > 0:
                time.sleep(stagger)
            futures.append(future)

        done_futures = list(concurrent.futures.as_completed(futures))
        for idx, future in enumerate(done_futures, 1):
            result = future.result()
            rel = Path(result['file']).relative_to(target_dir)
            if result.get('deleted'):
                deleted_ids.add(result['article_id'])
                success_count[0] += 1
                print(f"  [OK  ] [{idx}/{len(task_args)}] {rel}: 文章 {result['article_id']} 已删除")
            elif result['error']:
                # 404 = 文章已不存在（可能已被删除），不算真正失败
                if '404' in result['error'] or '资源不存在' in result.get('error', '') or str(result.get('error',''))[:50].find('404') != -1:
                    deleted_ids.add(result['article_id'])
                    success_count[0] += 1
                    print(f"  [SKIP] [{idx}/{len(task_args)}] {rel}: 文章 {result['article_id']} 已不存在（已删除）")
                else:
                    fail_count[0] += 1
                    print(f"  [FAIL] [{idx}/{len(task_args)}] {rel}: {result['error']}")

    print("\n" + "=" * 50)
    print(f"处理完成!")
    print(f"总计: {total}")
    print(f"成功删除（含已不存在）: {success_count[0]}")
    print(f"失败: {fail_count[0]}")


if __name__ == "__main__":
    main()