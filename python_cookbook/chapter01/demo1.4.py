'''1.4 查找最大或最小的 N 个元素

问题:
怎样从一个集合中获得最大或者最小的 N 个元素列表？

解决方案:
heapq 模块有两个函数：nlargest() 和 nsmallest() 可以完美解决这个问题。
'''

import heapq
from operator import itemgetter, attrgetter

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
nums.sort(reverse=True)
print(nums)
print(heapq.nlargest(3, nums))  # Prints [42, 37, 23]
nums.sort()
print(nums)
print(heapq.nsmallest(3, nums))  # Prints [-4, 1, 2]

portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])  # 在对每个元素进行对比的时候，会以 price 的值进行比较
'''[{'name': 'YHOO', 'shares': 45, 'price': 16.35}]'''
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])  # 在对每个元素进行对比的时候，会以 price 的值进行比较
'''[{'name': 'AAPL', 'shares': 50, 'price': 543.22}]'''

print(sorted(portfolio, key=lambda s: s['price']))
print(sorted(portfolio, key=itemgetter('price')))
print(sorted(portfolio, key=lambda s: s['price'], reverse=True))
print(sorted(portfolio, key=itemgetter('price'), reverse=True))


class Test:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        return repr((self.name, self.grade, self.age))


test = [Test('YJJ', 'B', 25),
        Test('JOJO', 'A', 26),
        Test('SAM', 'B', 26),
        Test('HUI', 'C', 26)]

print(sorted(test, key=attrgetter('name')))
print(sorted(test, key=lambda x: x.name))
print(sorted(test, key=attrgetter('age', 'name')))
