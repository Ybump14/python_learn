'''4.7 迭代器切片
问题:
你想得到一个由迭代器生成的切片对象，但是标准切片操作并不能做到。

解决方案:
函数 itertools.islice() 正好适用于在迭代器和生成器上做切片操作。

讨论:
迭代器和生成器不能使用标准的切片操作，因为它们的长度事先我们并不知道(并且也没有实现索引)。
函数 islice() 返回一个可以生成指定元素的迭代器，它通过遍历并丢弃直到切片开始索引位置的所有元素。
然后才开始一个个的返回元素，并直到切片结束索引位置。'''
import itertools


def count(n):
    while n <= 20:
        yield n
        n += 1


# count(0)[10:20]  # TypeError: 'generator' object is not subscriptable

c = count(0)
print(list(c))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print([i for i in itertools.islice(c, 5, 10)])  # [5, 6, 7, 8, 9]
print([i for i in itertools.islice(c, 5, 10)])  # [15, 16, 17, 18, 19]
print([i for i in c])  # [20]
