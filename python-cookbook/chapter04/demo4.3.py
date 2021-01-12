'''4.3 使用生成器创建新的迭代模式
问题:
你想实现一个自定义迭代模式，跟普通的内置函数比如 range() , reversed() 不一样。

解决方案:
如果你想实现一种新的迭代模式，使用一个生成器函数来定义它。 下面是一个生产某个范围内浮点数的生成器：'''


def frange(start, stop, increment):
    x = start
    while x < stop:
        yield round(x, 12)
        x += increment


Jojo = frange(0, 9.9, 0.1)
print(list(Jojo))
