'''7.8 减少可调用对象的参数个数
问题:
你有一个被其他python代码使用的callable对象，
可能是一个回调函数或者是一个处理器，
但是它的参数太多了，导致调用时出错。

解决方案:
如果需要减少某个函数的参数个数，你可以使用 functools.partial() 。
partial() 函数允许你给一个或多个参数设置固定的值，减少接下来被调用时的参数个数。
为了演示清楚，假设你有下面这样的函数：'''

import math
from functools import partial


def spam(a, b, c, d):
    print(a, b, c, d)


s1 = partial(spam, 1)
s1(2, 3, 4)  # 1 2 3 4
s1(4, 5, 6)  # 1 4 5 6

s2 = partial(spam, d=42)
s2(1, 2, 3)  # 1 2 3 42
s2(4, 5, 6)  # 4 5 6 42

s3 = partial(spam, 1, 2, d=42)
s3(3)  # 1 2 3 42
s3(5)  # 1 2 5 42

points = [(1, 3), (3, 2), (5, 6), (7, 8)]


def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.hypot(x2 - x1, y2 - y1)


print(distance((1, 2), (5, 6)))

pt = (4, 3)  # 基点
points.sort(key=partial(distance, pt))  # 计算 pt基点 和points 个坐标的距离,以此排序
print(points)  # [(3, 2), (1, 3), (5, 6), (7, 8)]

points.sort(key=lambda p: distance(pt, p))  # 同上
print(points)  # [(3, 2), (1, 3), (5, 6), (7, 8)]

points.sort(key=lambda p: p[0])  # 以元组的第一位排序
print(points)  # [(1, 3), (3, 2), (5, 6), (7, 8)]

points.sort(key=lambda p: p[1])  # 以元组的第2位排序
print(points)  # [(3, 2), (1, 3), (5, 6), (7, 8)]
