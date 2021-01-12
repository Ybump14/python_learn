'''4.11 同时迭代多个序列
问题:
你想同时迭代多个序列，每次分别从一个序列中取一个元素。

解决方案:
为了同时迭代多个序列，使用 zip() 函数。'''
import itertools

xpts = [1, 5, 4, 2, 10, 7]
ypts = [101, 78, 37, 15, 62, 99]

a = [1, 2, 3]
b = ['w', 'x', 'y', 'z']

zpts = zip(xpts, ypts)  # zip(a, b) 会生成一个可返回元组 (x, y) 的迭代器，其中x来自a，y来自b
print(list(zpts))  # [(1, 101), (5, 78), (4, 37), (2, 15), (10, 62), (7, 99)]

# 迭代长度跟参数中最长序列长度一致，使用itertools.zip_longest,可带参数填充值fillvalue=''
print(list(zip(a, b)))  # [(1, 'w'), (2, 'x'), (3, 'y')]
print(list(itertools.zip_longest(a, b)))  # [(1, 'w'), (2, 'x'), (3, 'y'), (None, 'z')]
print(list(itertools.zip_longest(a, b, fillvalue='fillvalue')))  # [(1, 'w'), (2, 'x'), (3, 'y'), ('fillvalue', 'z')]

print(dict(zip(a, b)))  # {1: 'w', 2: 'x', 3: 'y'}
print(dict(itertools.zip_longest(a, b)))  # {1: 'w', 2: 'x', 3: 'y', None: 'z'}
print(dict(itertools.zip_longest(a, b, fillvalue='fillvalue')))  # {1: 'w', 2: 'x', 3: 'y', 'fillvalue': 'z'}

print(tuple(zip(a, b)))  # ((1, 'w'), (2, 'x'), (3, 'y'))
print(tuple(itertools.zip_longest(a, b)))  # ((1, 'w'), (2, 'x'), (3, 'y'), (None, 'z'))
print(tuple(itertools.zip_longest(a, b, fillvalue='fillvalue')))  # ((1, 'w'), (2, 'x'), (3, 'y'), ('fillvalue', 'z'))

print(sorted(set(zip(a, b))))  # {(3, 'y'), (2, 'x'), (1, 'w')}
print(set(itertools.zip_longest(a, b)))  # {(3, 'y'), (2, 'x'), (1, 'w'), (None, 'z')}
print(set(itertools.zip_longest(a, b, fillvalue='fillvalue')))  # {(3, 'y'), (2, 'x'), (1, 'w'), ('fillvalue', 'z')}

a = [1, 2, 3]
b = [10, 11, 12]
c = ['x', 'y', 'z']
d = ['a', 'b', 'c']
print(list(zip(a, b, c, d)))
print(tuple(zip(a, b, c, d)))
print(set(zip(a, b, c, d)))
for i, j, k, z in zip(a, b, c, d):
    print('%s' % i, '=', '%s' % j, '+', '%s' % k, '+', '%s' % z)
