'''4.10 序列上索引值迭代
问题:
你想在迭代一个序列的同时跟踪正在被处理的元素索引。

解决方案:
内置的 enumerate() 函数可以很好的解决这个问题'''
from collections import defaultdict

my_list = ['a', 'b', 'c']
for idx, val in enumerate(my_list, 0):
    print(idx, val)

my_list = ['a', 'b', 'c']
for idx, val in enumerate(my_list, 1):
    print(idx, val)


