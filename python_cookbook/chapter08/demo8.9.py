'''8.9 创建新的类或实例属性
问题:
你想创建一个新的拥有一些额外功能的实例属性类型，比如类型检查。

解决方案:
如果你想创建一个全新的实例属性，可以通过一个描述器类的形式来定义它的功能。

一个描述器就是一个实现了三个核心的属性访问操作(get, set, delete)的类，
分别为 __get__() 、__set__() 和 __delete__() 这三个特殊的方法。
这些方法接受一个实例作为输入，之后相应的操作实例底层的字典。'''


class Integer:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Expected an int')
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class Point:
    x = Integer('x')
    y = Integer('y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


# p = Point(2, 3)
# print(p.x)
# print(p.y)
# p.x = 11
# print(p.x)
# p.y = 'wq'  TypeError: Expected an int

# class A:
#     def __init__(self):
#         self.a1 = 'a1'
#         print('A.init')
#
#
# class B:
#     x = A()
#     def __init__(self):
#         print('B.init')
#
# print('****************')
# print(B.x.a1)
#
# print('----------------')
# b = B()
# print(b.x.a1)


class A:
    def __init__(self):
        self.a1 = 'a1'
        print('A.init')

    def __get__(self, instance, owner):
        print("A.__get__ {} {} {}".format(self, instance, owner))


class B:
    x = A()

    def __init__(self):
        print('B.init')


print('****************')
print(B.x)

print('----------------')
b = B()
print(b.x)
