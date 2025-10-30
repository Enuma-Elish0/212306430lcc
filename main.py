#!/usr/bin/env python3
"""
Git 实践项目主程序
项目: 212306430LCC
"""

from src.utils import format_message, calculate_statistics, calculate_circle_area

def main():
    print("=== Git 与远程仓库协作实践 ===")
    print("项目: 212306430LCC")
    
    # 使用工具模块
    message = format_message("开始功能开发")
    print(message)
    
    # 数据处理示例
    data = [10, 20, 30, 40, 50]
    stats = calculate_statistics(data)
    
    print("\n数据统计结果:")
    for key, value in stats.items():
        print(f"{key}: {value}")
    
    # 几何计算示例
    radius = 7.5
    area = calculate_circle_area(radius)
    print(f"\n半径为 {radius} 的圆面积: {area:.2f}")

if __name__ == "__main__":
    main()
