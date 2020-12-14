'''1.16 过滤序列元素
问题:
你有一个数据序列，想利用一些规则从中提取出需要的值或者是缩短序列

解决方案:
最简单的过滤序列元素的方法就是使用列表推导。'''
import math
from itertools import compress

mylist = [1, 4, -5, 10, -7, 2, 3, -1]

print([n for n in mylist if n > 0])  # 潜在缺陷:输入非常大的时候会产生一个非常大的结果集，占用大量内存
print([math.sqrt(n) for n in mylist if n > 0])  # 转换数据
print([n if n > 0 else 0 for n in mylist])  # 替换
print([n if n < 0 else 0 for n in mylist])  # 替换

pos = (n for n in mylist if n > 0)  # 使用生成器表达式
new_post = []
for n in pos:
    new_post.append(n)
print(new_post)

values = ['1', '2', '-3', '-', '4', 'N/A', '5']


def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False


ivals = list(filter(is_int, values))  # filter 返回一个迭代器,list转换为列表
print(ivals)

addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]
counts = [0, 3, 10, 4, 1, 7, 6, 1]
# 先创建一个 Boolean 序列,指示哪些元素符合条件
more5 = [n > 5 for n in counts]
# 然后 compress() 函数根据这个序列去选择输出对应位置为 True 的元素。
# compress 返回一个迭代器,list转换为列表
print(list(compress(addresses, more5)))
