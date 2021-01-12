'''1.19 转换并同时计算数据
问题:
你需要在数据序列上执行聚集函数（比如 sum() , min() , max() ）， 但是首先你需要先转换或者过滤数据

解决方案:
一个非常优雅的方式去结合数据计算与转换就是使用一个生成器表达式参数。'''
import os

nums = [1, 2, 3, 4, 5]
s = sum(x * x for x in nums)

files = os.listdir('E:\python_learn/python-cookbook/chapterData/')  # Sorry, no python.
if any(name.endswith('.py') for name in files):
    print('There be python!')
else:
    print('Sorry, no python.')

# Output a tuple as CSV
s = ('ACME', 50, 123.45)
print(','.join(str(x) for x in s))  # ACME,50,123.45

# Data reduction across fields of a chapterData structure
portfolio = [
    {'name': 'GOOG', 'shares': 50},
    {'name': 'YHOO', 'shares': 75},
    {'name': 'AOL', 'shares': 20},
    {'name': 'SCOX', 'shares': 65}
]
min_shares = min(s['shares'] for s in portfolio)  # 20
min_shares = min(portfolio, key=lambda s: s['shares'])  # {'name': 'AOL', 'shares': 20}
