class DataProcessor:
    def __init__(self):
        self.data = []
    
    def add_data(self, value):
        self.data.append(value)
        return f"添加数据: {value}"
    
    def process_data(self):
        if not self.data:
            return "没有数据"
        return sorted(self.data)

def demo():
    processor = DataProcessor()
    test_data = [5, 2, 8, 1, 9]
    for value in test_data:
        print(processor.add_data(value))
    result = processor.process_data()
    print("处理结果:", result)

if __name__ == "__main__":
    demo()
