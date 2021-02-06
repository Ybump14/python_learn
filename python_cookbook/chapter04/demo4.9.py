'''4.9 排列组合的迭代
问题
你想迭代遍历一个集合中元素的所有可能的排列或组合

解决方案
itertools模块提供了三个函数来解决这类问题。
其中一个是 itertools.permutations() ，
它接受一个集合并产生一个元组序列，每个元组由集合中所有元素的一个可能排列组成。
也就是说通过打乱集合中元素排列顺序生成一个元组'''

items = ['a', 'b', 'c']
from itertools import permutations, combinations, combinations_with_replacement

for p in permutations(items):
    print(p)

print(format('分割线', '*^12'))

for p in combinations(items, 2):
    print(p)

print(format('分割线', '*^12'))
for p in combinations_with_replacement(items,2):
    print(p)
