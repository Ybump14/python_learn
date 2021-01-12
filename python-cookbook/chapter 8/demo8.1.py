'''8.1 改变对象的字符串显示
问题:
你想改变对象实例的打印或显示输出，让它们更具可读性。

解决方案:
要改变一个实例的字符串表示，可重新定义它的 __str__() 和 __repr__() 方法。例如：'''


class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Pair({0.x!r}, {0.y!r})'.format(self)

    def __str__(self):
        return '({0.x!s}, {0.y!s})'.format(self)


p = Pair(3, 4)
print(p)
print('p is {0!r}'.format(p))
