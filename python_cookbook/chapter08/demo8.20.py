'''8.20 通过字符串调用对象方法
问题:
你有一个字符串形式的方法名称，想通过它调用某个对象的对应方法。

解决方案:
最简单的情况，可以使用 getattr() ：'''

import operator
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point({!r:},{!r:})'.format(self.x, self.y)

    def distance(self, x, y):
        return math.hypot(self.x - x, self.y - y)


p = Point(2, 3)
d = getattr(p, 'distance')(1, 1)  # Calls p.distance(0, 0)
print(d)

print(operator.methodcaller('distance', 0, 0)(p))

points = [
    Point(1, 2),
    Point(3, 0),
    Point(10, -3),
    Point(-5, -7),
    Point(-1, 8),
    Point(3, 2)
]
# Sort by distance from origin (0, 0)
points.sort(key=operator.methodcaller('distance', 0, 0))
print(points)
