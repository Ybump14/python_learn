'''7.5 定义有默认参数的函数
问题:
你想定义一个函数或者方法，它的一个或多个参数是可选的并且有一个默认值。

解决方案:
定义一个有可选参数的函数是非常简单的，直接在函数定义中给参数指定一个默认值，并放到参数列表最后就行了'''


def spam(a, b=42):
    print(a, b)


spam(1)  # Ok. a=1, b=42
spam(1, 2)  # Ok. a=1, b=2


# 如果默认参数是一个可修改的容器比如一个列表、集合或者字典，可以使用None作为默认值
# Using a list as a default value
def spam(a, b=None):
    if b is None:
        b = []
    ...


# 如果你并不想提供一个默认值，而是想仅仅测试下某个默认参数是不是有传递进来，可以像下面这样写：
_no_value = object()


def spam(a, b=_no_value):
    if b is _no_value:
        print('No b value supplied')
    else:
        print('b=%s' % b)


# 传递一个None值和不传值两种情况
spam(1)  # No b value supplied
spam(1, None)  # b=None

# 讨论
# 定义带默认值参数的函数是很简单的，但绝不仅仅只是这个，还有一些东西在这里也深入讨论下。
# 首先，默认参数的值仅仅在函数定义的时候赋值一次。
x = 42


def spam(a, b=x):
    print(a, b)


spam(1)  # 1  42
x = 23
spam(1)  # 1  42

# 默认参数的值应该是不可变的对象，比如None、True、False、数字或字符串。
