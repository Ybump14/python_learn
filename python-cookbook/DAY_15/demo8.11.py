'''8.11 简化数据结构的初始化
问题:
你写了很多仅仅用作数据结构的类，不想写太多烦人的 __init__() 函数

解决方案:
可以在一个基类中写一个公用的 __init__() 函数：'''
import math


class Structure1:
    # Class variable that specifies expected fields
    _fields = []

    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))
        # Set the arguments
        for name, value in zip(self._fields, args):
            setattr(self, name, value)


class Stock(Structure1):
    _fields = ['name', 'shares', 'price']


class Point(Structure1):
    _fields = ['x', 'y']


class Circle(Structure1):
    _fields = ['radius']

    def area(self):
        return math.pi * self.radius ** 2


class Structure2:
    _fields = []

    def __init__(self, *args, **kwargs):
        if len(args) > len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))
        # Set all of the positional arguments
        for name, value in zip(self._fields, args):
            setattr(self, name, value)
        # Set the remaining keyword arguments
        for name in self._fields[len(args):]:
            print(kwargs)
            setattr(self, name, kwargs.pop(name))

        # Check for any remaining unknown arguments
        if kwargs:
            raise TypeError('Invalid argument(s): {}'.format(','.join(kwargs)))


class Structure3:
    # Class variable that specifies expected fields
    _fields = []

    def __init__(self, *args, **kwargs):
        if len(args) != len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))

        # Set the arguments
        for name, value in zip(self._fields, args):
            setattr(self, name, value)

        # Set the additional arguments (if any)
        extra_args = kwargs.keys() - self._fields

        for name in extra_args:
            setattr(self, name, kwargs.pop(name))

        if kwargs:
            raise TypeError('Duplicate values for {}'.format(','.join(kwargs)))


# Example use
if __name__ == '__main__':
    # Example 1
    # s = Stock('ACME', 50, 91.1)
    # print(s.name, s.shares, s.price, sep=' ')  # ACME 50 91.1
    #
    # p = Point(2, 3)  # 2 3
    # print(p.x, p.y)
    #
    # c = Circle('radius')  # radius
    # print(c.radius)

    # Example 2
    class Stock(Structure2):
        _fields = ['name', 'shares', 'price']


    # s1 = Stock('ACME', 50, 91.1)
    # print(s1.name, s1.shares, s1.price)
    # s2 = Stock('ACME', 50, price=91.1)
    # print(s2.name, s2.shares, s2.price)
    # s3 = Stock('ACME', shares=50, price=91.1)
    # print(s3.name, s3.shares, s3.price)

    # s3 = Stock('ACME', shares=50, price=91.1, aa=1)
    # print(s3.name, s3.shares, s3.price)
    # raise TypeError('Invalid argument(s): {}'.format(','.join(kwargs)))
    # TypeError: Invalid argument(s): aa

    # Example 3
    class Stock(Structure3):
        _fields = ['name', 'shares', 'price']


    # s1 = Stock('ACME', 50, 91.1)
    s2 = Stock('ACME', 50, 91.1, date='8/2/2012', MyName='YANGJIAJUN')
    print(s2.name, s2.shares, s2.price, s2.MyName, sep=' ')  # ACME 50 91.1 YANGJIAJUN
