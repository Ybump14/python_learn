'''1.8 字典的运算
问题:
怎样在数据字典中执行一些计算操作（比如求最小值、最大值、排序等等）？

解决方案:
为了对字典值执行计算操作，通常需要使用 zip() 函数先将键和值反转过来
'''

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
min_price = min(zip(prices.values(), prices.keys()))
# min_price is (10.75, 'FB')
max_price = max(zip(prices.values(), prices.keys()))
# max_price is (612.78, 'AAPL')


''' zip() 函数创建的是一个只能访问一次的迭代器。'''
prices_and_names = zip(prices.values(), prices.keys())
print(min(prices_and_names))  # OK
# print(max(prices_and_names))  # ValueError: max() arg is an empty sequence
