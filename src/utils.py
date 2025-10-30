"""
工具函数模块
项目: 212306430LCC
"""

import datetime
import math

def get_timestamp():
    """获取当前时间戳"""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def format_message(message):
    """格式化消息"""
    return f"[{get_timestamp()}] {message}"

def calculate_circle_area(radius):
    """计算圆面积"""
    return math.pi * radius ** 2

def calculate_statistics(numbers):
    """计算统计信息"""
    if not numbers:
        return {}
    
    return {
        "count": len(numbers),
        "sum": sum(numbers),
        "average": sum(numbers) / len(numbers),
        "max": max(numbers),
        "min": min(numbers)
    }

if __name__ == "__main__":
    # 模块测试
    print("工具模块测试:")
    print(format_message("工具模块初始化成功"))
    
    test_data = [1, 3, 5, 7, 9]
    stats = calculate_statistics(test_data)
    print(f"数据统计: {stats}")
    
    radius = 5
    area = calculate_circle_area(radius)
    print(f"半径为 {radius} 的圆面积: {area:.2f}")

# 故意引入的错误函数 - 用于回滚练习
def problematic_function():
    # 这里有语法错误 - 字符串没有正确闭合
    print("这是一个故意引入的错误

    # 这里有逻辑错误 - 可能除零
    def bad_division(a, b):
        return a / b  # 当 b=0 时会出错

    return "错误代码"
