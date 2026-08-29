"""
从 Z-Library 搜索并下载数学物理相关 PDF 书籍。
使用 Cookie.json 中的登录凭据进行访问。
"""

import json
import os
import re
import sys
import time
import requests
from urllib.parse import quote, urljoin
from bs4 import BeautifulSoup

# === 配置 ===
COOKIE_FILE = os.path.join(os.path.dirname(__file__), "Cookie.json")
DOWNLOAD_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "pdfs")
BASE_URL = "https://zh.z-lib.gd"

# 要搜索的书籍列表（中文物理教材）
BOOKS_TO_SEARCH = [
    "物理学 中文 教材",
    "理论物理 中文",
    "量子力学 中文 书",
    "电动力学 中文",
    "热力学与统计物理 中文",
    "经典力学 中文",
    "数学物理方法 中文",
]


def load_cookies(cookie_file: str) -> dict:
    """从 Cookie.json 加载 cookies 为 requests 可用的字典格式。"""
    with open(cookie_file, "r", encoding="utf-8") as f:
        cookie_list = json.load(f)
    cookies = {}
    for c in cookie_list:
        cookies[c["name"]] = c["value"]
    return cookies


def create_session(cookies: dict) -> requests.Session:
    """创建带有 cookies 和常用 headers 的 requests Session。"""
    session = requests.Session()
    session.cookies.update(cookies)
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/120.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Referer": BASE_URL,
    })
    return session


def search_books(session: requests.Session, query: str) -> list:
    """
    在 Z-Library 上搜索书籍，返回搜索结果列表。
    每个结果是一个字典，包含 title, author, href, year, extension 等信息。
    """
    search_url = f"{BASE_URL}/s/{quote(query)}"
    print(f"\n🔍 搜索: {query}")
    print(f"   URL: {search_url}")

    resp = session.get(search_url, timeout=30)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "html.parser")
    results = []

    # Z-Library 搜索结果通常在特定的容器中
    # 尝试多种选择器以适配不同的页面结构
    items = soup.select("div.bookRow, div[class*='book-item'], table[class*='book'] tr")

    if not items:
        # 尝试从所有链接中提取书籍链接
        links = soup.select("a[href*='/book/']")
        for link in links:
            href = link.get("href", "")
            title = link.get_text(strip=True)
            if title and href:
                results.append({
                    "title": title,
                    "href": href if href.startswith("http") else urljoin(BASE_URL, href),
                    "author": "",
                    "year": "",
                    "extension": "",
                })
    else:
        for item in items:
            title_el = item.select_one("a[href*='/book/']")
            if not title_el:
                continue
            title = title_el.get_text(strip=True)
            href = title_el.get("href", "")
            author_el = item.select_one("div[class*='author'], span[class*='author']")
            author = author_el.get_text(strip=True) if author_el else ""
            results.append({
                "title": title,
                "href": href if href.startswith("http") else urljoin(BASE_URL, href),
                "author": author,
                "year": "",
                "extension": "",
            })

    # 去重
    seen = set()
    unique_results = []
    for r in results:
        key = r["href"]
        if key not in seen:
            seen.add(key)
            unique_results.append(r)

    return unique_results


def get_download_info(session: requests.Session, book_url: str) -> dict:
    """
    访问书籍详情页，获取下载链接和文件信息。
    """
    if not book_url.startswith("http"):
        book_url = urljoin(BASE_URL, book_url)

    print(f"\n📖 访问书籍页面: {book_url}")
    resp = session.get(book_url, timeout=30)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "html.parser")

    # 获取书籍标题
    title_el = soup.select_one("h1, div[class*='book-title'], span[class*='title']")
    title = title_el.get_text(strip=True) if title_el else "Unknown"

    # 获取下载链接
    download_link = None
    download_btn = soup.select_one("a[href*='/dl/'], a[class*='download'], a[onclick*='download']")
    if download_btn:
        download_link = download_btn.get("href", "")
        if download_link and not download_link.startswith("http"):
            download_link = urljoin(BASE_URL, download_link)

    # 获取文件格式
    extension = ""
    ext_el = soup.select_one("span[class*='extension'], div[class*='file-type']")
    if ext_el:
        extension = ext_el.get_text(strip=True).lower()

    return {
        "title": title,
        "download_url": download_link,
        "extension": extension,
        "page_url": book_url,
    }


def download_file(session: requests.Session, url: str, save_path: str) -> bool:
    """
    下载文件到指定路径。
    """
    print(f"\n⬇️  下载中: {url}")
    print(f"   保存到: {save_path}")

    try:
        resp = session.get(url, timeout=120, stream=True)
        resp.raise_for_status()

        # 检查 Content-Type 确保是文件
        content_type = resp.headers.get("Content-Type", "")
        content_length = resp.headers.get("Content-Length", "未知")
        print(f"   Content-Type: {content_type}")
        print(f"   文件大小: {content_length}")

        os.makedirs(os.path.dirname(save_path), exist_ok=True)

        total = 0
        with open(save_path, "wb") as f:
            for chunk in resp.iter_content(chunk_size=8192):
                f.write(chunk)
                total += len(chunk)

        print(f"   ✅ 下载完成！文件大小: {total / 1024 / 1024:.2f} MB")
        return True

    except Exception as e:
        print(f"   ❌ 下载失败: {e}")
        return False


def sanitize_filename(name: str) -> str:
    """清理文件名中的非法字符。"""
    name = re.sub(r'[<>:"/\\|?*]', '_', name)
    name = name.strip('. ')
    return name[:200]  # 限制文件名长度


def main():
    # 加载 cookies
    print("📂 加载 Cookie...")
    cookies = load_cookies(COOKIE_FILE)
    print(f"   已加载 {len(cookies)} 个 cookie")

    # 创建 session
    session = create_session(cookies)

    # 测试连接
    print("\n🌐 测试连接...")
    try:
        resp = session.get(BASE_URL, timeout=15)
        print(f"   状态码: {resp.status_code}")
        if resp.status_code != 200:
            print("   ⚠️  连接可能有问题，继续尝试...")
    except Exception as e:
        print(f"   ❌ 连接失败: {e}")
        sys.exit(1)

    # 确保下载目录存在
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)

    # 搜索并下载每本书
    for query in BOOKS_TO_SEARCH:
        print(f"\n{'='*60}")
        print(f"📚 处理: {query}")
        print(f"{'='*60}")

        results = search_books(session, query)

        if not results:
            print(f"   ⚠️  未找到搜索结果")
            continue

        print(f"\n   找到 {len(results)} 个结果:")
        for i, r in enumerate(results[:10], 1):
            print(f"   [{i}] {r['title']}")
            if r.get('author'):
                print(f"       作者: {r['author']}")
            print(f"       链接: {r['href']}")

        # 选择第一个最匹配的结果
        best = results[0]
        print(f"\n   🎯 选择: {best['title']}")

        # 获取下载信息
        try:
            info = get_download_info(session, best["href"])
        except Exception as e:
            print(f"   ❌ 获取书籍信息失败: {e}")
            continue

        if not info.get("download_url"):
            print(f"   ⚠️  未找到下载链接，尝试直接从页面下载...")
            # 尝试从书籍页面直接下载
            info["download_url"] = info["page_url"]

        # 构建保存路径
        ext = info.get("extension", "pdf")
        if not ext or ext not in ("pdf", "epub", "djvu", "mobi"):
            ext = "pdf"
        filename = sanitize_filename(info["title"]) + f".{ext}"
        save_path = os.path.join(DOWNLOAD_DIR, filename)

        # 下载文件
        download_file(session, info["download_url"], save_path)

        # 下载间隔，避免请求过于频繁
        time.sleep(3)

    print(f"\n{'='*60}")
    print("🎉 全部任务完成！")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
