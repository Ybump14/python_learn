'''8.6 创建可管理的属性
问题:
你想给某个实例attribute增加除访问与修改之外的其他处理逻辑，比如类型检查或合法性验证。

解决方案:
自定义某个属性的一种简单方法是将它定义为一个property。
例如，下面的代码定义了一个property，增加对一个属性简单的类型检查：'''


class Person:
    def __init__(self, first_name):
        self._first_name = first_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

    @first_name.deleter
    def first_name(self):
        raise AttributeError("Can't delete attribute")


class A:
    def get_test(self):
        return self.test

    def set_test(self, value):
        self.test = value

    name = property(get_test, set_test)


import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def diameter(self):
        return self.radius * 2

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius


class Circle_test:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

    def get_diameter(self):
        return self.radius * 2

    def get_perimeter(self):
        return 2 * math.pi * self.radius

    area = property(get_area)
    diameter = property(get_diameter)
    perimeter = property(get_perimeter)


c = Circle(4)
# print(c.area)
# print(c.diameter)
# print(c.perimeter)

c_test = Circle_test(4)

print(c_test.area)
print(c_test.diameter)
print(c_test.perimeter, '\n')

print(c_test.get_area())
print(c_test.get_diameter())
print(c_test.get_perimeter())
