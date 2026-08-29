#!/usr/bin/env python3
"""
知乎批量查询快速开始示例
"""

import subprocess
import sys
import os

def show_help():
    """显示帮助信息"""
    print("知乎文章批量查询工具")
    print("=" * 50)
    print()
    print("使用方法:")
    print("1. 首先获取知乎认证信息（cookie, x-zse-96, x-zst-81）")
    print("2. 编辑 zhihu_config.json 填入认证信息")
    print("3. 运行: python run_batch_query.py")
    print()
    print("或者直接使用命令行:")
    print("python zhihu_batch_query.py --cookie \"你的cookie\" --x-zse-96 \"签名\" --x-zst-81 \"签名\" --output articles.json --summary")
    print()
    print("查看详细说明: README_ZHIHU_BATCH_QUERY.md")

def check_config():
    """检查配置文件"""
    config_path = "zhihu_config.json"
    if not os.path.exists(config_path):
        print(f"配置文件 {config_path} 不存在")
        print("请先复制模板文件:")
        print("copy zhihu_config.json zhihu_config.json.example")
        return False
    
    try:
        import json
        with open(config_path, 'r', encoding='utf-8') as f:
            config = json.load(f)
        
        zhihu_config = config.get('zhihu', {})
        cookie = zhihu_config.get('cookie', '').strip()
        
        if not cookie:
            print("配置文件中 cookie 为空，请填入你的知乎cookie")
            return False
            
        print("配置文件检查通过")
        return True
    except Exception as e:
        print(f"读取配置文件失败: {e}")
        return False

def main():
    if len(sys.argv) > 1 and sys.argv[1] in ['-h', '--help']:
        show_help()
        return
    
    print("知乎文章批量查询工具 - 快速开始")
    print("-" * 40)
    
    if not check_config():
        print()
        show_help()
        return
    
    print("\n配置检查通过，可以开始查询...")
    print("直接运行: python run_batch_query.py")
    print("或查看帮助: python zhihu_batch_query.py --help")

if __name__ == '__main__':
    main()