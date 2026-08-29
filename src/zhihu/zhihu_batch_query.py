#!/usr/bin/env python3
"""
知乎文章批量查询脚本
支持分页查询，自动处理 offset 循环请求直到结束
"""

import requests
import json
import time
from typing import Dict, List, Optional


class ZhihuBatchQuery:
    def __init__(self, user_id: str = "yjk-59-34", limit: int = 20, delay: float = 1.0):
        """
        初始化查询器
        
        Args:
            user_id: 知乎用户ID
            limit: 每页获取数量
            delay: 请求间隔时间(秒)，避免频率限制
        """
        self.user_id = user_id
        self.limit = limit
        self.delay = delay
        self.base_url = f"https://www.zhihu.com/api/v3/moments/{user_id}/activities"
        
        # 基础请求头（需要根据实际情况更新 cookie 和签名）
        self.headers = {
            'pragma': 'no-cache',
            'cache-control': 'no-cache',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua': '"Not=A?Brand";v="99", "Google Chrome";v="151", "Chromium";v="151"',
            'x-api-version': '3.0.40',
            'sec-ch-ua-mobile': '?0',
            'x-requested-with': 'fetch',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36',
            'x-zse-93': '101_3_3.0',
            'accept': '*/*',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': f'https://www.zhihu.com/people/{user_id}',
            'accept-encoding': 'gzip, deflate, br, zstd',
            'accept-language': 'zh-CN,zh;q=0.9',
            'priority': 'u=1, i',
            # 注意：cookie 和 x-zse-96/x-zst-81 需要从浏览器获取最新值
            'cookie': '',  # 请填入你的 cookie
        }
    
    def set_cookie(self, cookie: str):
        """设置 cookie"""
        self.headers['cookie'] = cookie
    
    def set_signature(self, x_zse_96: str = None, x_zst_81: str = None):
        """设置签名参数（从浏览器开发者工具获取）"""
        if x_zse_96:
            self.headers['x-zse-96'] = x_zse_96
        if x_zst_81:
            self.headers['x-zst-81'] = x_zst_81
    
    def fetch_page(self, offset: Optional[str] = None, page_num: int = 1) -> Optional[Dict]:
        """
        获取单页数据
        
        Args:
            offset: 分页偏移量
            page_num: 页码
            
        Returns:
            响应数据字典，失败返回 None
        """
        if offset:
            # 使用 offset 分页
            url = f"{self.base_url}?offset={offset}&page_num={page_num}"
        else:
            # 首页请求
            url = f"{self.base_url}?limit={self.limit}&desktop=true&ws_qiangzhisafe=0"
        
        try:
            response = requests.get(url, headers=self.headers, timeout=30)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"请求失败: {e}")
            if hasattr(e, 'response') and e.response is not None:
                print(f"状态码: {e.response.status_code}")
                print(f"响应内容: {e.response.text[:500]}")
            return None
        except json.JSONDecodeError as e:
            print(f"JSON 解析失败: {e}")
            return None
    
    def extract_articles(self, data: Dict) -> List[Dict]:
        """
        从响应数据中提取文章信息
        
        Args:
            data: API 响应数据
            
        Returns:
            文章列表
        """
        articles = []
        
        if not data or 'data' not in data:
            return articles
        
        for item in data['data']:
            # 知乎活动流包含多种类型，筛选文章类型
            # 文章类型在 target.type 中，不是顶层 type
            target = item.get('target', {})
            if target.get('type') == 'article':
                article = {
                    'id': target.get('id'),
                    'title': target.get('title'),
                    'url': target.get('url'),
                    'excerpt': target.get('excerpt'),
                    'created_time': target.get('created'),
                    'updated_time': target.get('updated'),
                    'voteup_count': target.get('voteup_count', 0),
                    'comment_count': target.get('comment_count', 0),
                    'author': item.get('actor', {}).get('name'),
                    'raw_data': item  # 保留原始数据
                }
                articles.append(article)
        
        return articles
    
    def get_next_offset(self, data: Dict) -> Optional[str]:
        """
        从响应中获取下一页的 offset
        
        Args:
            data: API 响应数据
            
        Returns:
            下一页 offset，如果没有更多数据返回 None
        """
        if not data:
            return None
        
        # 尝试从 paging 中获取
        paging = data.get('paging', {})
        if paging.get('is_end', True):
            return None
        
        next_url = paging.get('next')
        if next_url:
            # 从 next URL 中提取 offset
            import urllib.parse
            parsed = urllib.parse.urlparse(next_url)
            params = urllib.parse.parse_qs(parsed.query)
            if 'offset' in params:
                return params['offset'][0]
        
        # 备选：直接从 paging 获取 offset
        return paging.get('offset')
    
    def query_all(self, max_pages: int = 0, output_file: str = None) -> List[Dict]:
        """
        批量查询所有文章
        
        Args:
            max_pages: 最大页数限制，0 表示无限制
            output_file: 结果保存文件路径
            
        Returns:
            所有文章列表
        """
        all_articles = []
        offset = None
        page_num = 1
        page_count = 0
        
        print(f"开始批量查询用户 {self.user_id} 的文章...")
        print(f"每页数量: {self.limit}, 请求间隔: {self.delay}秒")
        print("-" * 50)
        
        while True:
            if max_pages > 0 and page_count >= max_pages:
                print(f"达到最大页数限制: {max_pages}")
                break
            
            print(f"正在获取第 {page_num} 页... (offset: {offset or '首页'})")
            
            data = self.fetch_page(offset, page_num)
            
            if not data:
                print("获取数据失败，停止查询")
                break
            
            # 提取文章
            articles = self.extract_articles(data)
            all_articles.extend(articles)
            
            print(f"  本页获取文章数: {len(articles)}")
            print(f"  累计文章数: {len(all_articles)}")
            
            # 获取下一页 offset
            next_offset = self.get_next_offset(data)
            
            if not next_offset:
                print("没有更多数据，查询结束")
                break
            
            offset = next_offset
            page_num += 1
            page_count += 1
            
            # 延迟避免频率限制
            if self.delay > 0:
                time.sleep(self.delay)
        
        print("-" * 50)
        print(f"查询完成！总共获取文章: {len(all_articles)} 篇")
        
        # 保存结果
        if output_file:
            self.save_results(all_articles, output_file)
        
        return all_articles
    
    def save_results(self, articles: List[Dict], filepath: str):
        """保存结果到文件"""
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump({
                    'user_id': self.user_id,
                    'total_count': len(articles),
                    'articles': articles
                }, f, ensure_ascii=False, indent=2)
            print(f"结果已保存到: {filepath}")
        except Exception as e:
            print(f"保存失败: {e}")
    
    def print_summary(self, articles: List[Dict]):
        """打印文章摘要"""
        if not articles:
            print("没有文章数据")
            return
        
        print("\n文章列表摘要:")
        print("=" * 80)
        for i, article in enumerate(articles, 1):
            title = article.get('title', '无标题')[:60]
            created = article.get('created_time', '未知时间')
            votes = article.get('voteup_count', 0)
            comments = article.get('comment_count', 0)
            print(f"{i:3d}. {title}")
            print(f"     时间: {created} | 赞: {votes} | 评论: {comments}")
            print()


def main():
    """主函数"""
    import argparse
    
    parser = argparse.ArgumentParser(description='知乎文章批量查询脚本')
    parser.add_argument('--user-id', default='yjk-59-34', help='知乎用户ID')
    parser.add_argument('--limit', type=int, default=20, help='每页数量')
    parser.add_argument('--delay', type=float, default=1.0, help='请求间隔(秒)')
    parser.add_argument('--max-pages', type=int, default=0, help='最大页数(0=无限制)')
    parser.add_argument('--output', '-o', help='输出文件路径')
    parser.add_argument('--cookie', help='Cookie 字符串')
    parser.add_argument('--x-zse-96', help='x-zse-96 签名')
    parser.add_argument('--x-zst-81', help='x-zst-81 签名')
    parser.add_argument('--summary', action='store_true', help='显示摘要')
    
    args = parser.parse_args()
    
    # 创建查询器
    query = ZhihuBatchQuery(
        user_id=args.user_id,
        limit=args.limit,
        delay=args.delay
    )
    
    # 设置认证信息
    if args.cookie:
        query.set_cookie(args.cookie)
    if args.x_zse_96:
        query.set_signature(x_zse_96=args.x_zse_96)
    if args.x_zst_81:
        query.set_signature(x_zst_81=args.x_zst_81)
    
    # 检查必要的认证信息
    if not query.headers.get('cookie'):
        print("错误: 请提供 cookie (--cookie 参数)")
        print("可以从浏览器开发者工具 Network 面板复制")
        return
    
    # 执行批量查询
    articles = query.query_all(
        max_pages=args.max_pages,
        output_file=args.output
    )
    
    # 显示摘要
    if args.summary:
        query.print_summary(articles)


if __name__ == '__main__':
    main()