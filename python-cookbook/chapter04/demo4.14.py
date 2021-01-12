'''4.14 展开嵌套的序列
问题:
你想将一个多层嵌套的序列展开成一个单层列表

解决方案:
可以写一个包含 yield from 语句的递归生成器来轻松解决这个问题。'''

from collections.abc import Iterable

items = ['Dave', 'Paula', ['Thomas', 'Lewis']]


# for 循环写法
def flatten_for(items):
    for i in items:
        if isinstance(i, Iterable) and not isinstance(i, str or bytes):
            for j in i:
                yield j
        else:
            yield i


def flatten_yield(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            # for i in flatten(x): 额外的for
            #     yield i
            yield from flatten_yield(x)  # 调用flatten_yield生成器作为子例程 ['Dave', 'Paula', 'Thomas', 'Lewis']
            # yield from flatten_for(x)  # 调用flatten_for生成器作为子例程 ['Dave', 'Paula', 'Thomas', 'Lewis']
            # yield flatten_for(x)  # ['Dave', 'Paula', <generator object flatten at 0x08E04DF0>]
            # yield flatten_yield(x)  # ['Dave', 'Paula', <generator object flatten at 0x08E04DF0>]
        else:
            yield x


print(list(flatten_for(items)))  # ['Dave', 'Paula', 'Thomas', 'Lewis']
print(list(flatten_yield(items)))  # ['Dave', 'Paula', 'Thomas', 'Lewis']
