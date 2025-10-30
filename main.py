#!/usr/bin/env python3
"""
Git 实践项目主程序
项目: 212306430LCC
"""

from src.utils import format_message
from src.data_processor import demo

def main():
    print("=== Git 与远程仓库协作实践 ===")
    print("项目: 212306430LCC")
    
    message = format_message("开始功能开发")
    print(message)
    
    print("\n数据处理演示:")
    demo()

if __name__ == "__main__":
    main()
