'''1.17 从字典中提取子集
问题:
你想构造一个字典，它是另外一个字典的子集。

解决方案:
最简单的方式是使用字典推导'''
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
# 字典推导 (表意比dict()函数更清晰,且运行更快)
p1 = {key: value for key, value in prices.items() if value > 200}
p2 = {key: value for key, value in prices.items() if key in tech_names}
p2 = {key: prices[key] for key in prices.keys() & tech_names}  # 运行时间测试结果显示这种方案大概比第一种p2方案慢 1.6 倍

# 创建一个元组序列然后把它传给 dict() 函数
p1 = dict((key, value) for key, value in prices.items() if value > 200)
