'''8.15 属性的代理访问
问题:
你想将某个实例的属性访问代理到内部另一个实例中去，目的可能是作为继承的一个替代方法或者实现代理模式。

解决方案:
简单来说，代理是一种编程模式，它将某个操作转移给另外一个对象来实现。 最简单的形式可能是像下面这样：'''


class A:
    def spam(self, x):
        return x

    def foo(self):
        return 'A foo'

    def bar(self):
        return 'A bar'


class B1:
    """简单的代理,如果仅仅就两个方法需要代理，那么像这样写就足够了。"""

    def __init__(self):
        self._a = A()

    def spam(self, x):
        # Delegate to the internal self._a instance
        return self._a.spam(x)

    def foo(self):
        # Delegate to the internal self._a instance
        return self._a.foo()

    def bar(self):
        return 'B1 bar'


class B2:
    """但是，如果有大量的方法需要代理， 那么使用 __getattr__() 方法或许或更好些：
    使用_getattr__的代理，代理方法比较多的时候"""

    def __init__(self):
        self._a = A()

    def bar(self):
        return 'B2 bar'

    # Expose all of the methods defined on class A
    def __getattr__(self, name):
        """这个方法在访问的attribute不存在的时候被调用
           the __getattr__() method is actually a fallback method
           that only gets called when an attribute is not found"""
        return getattr(self._a, name)


# A proxy class that wraps around another object, but
# exposes its public attributes
class Proxy:
    def __init__(self, obj):
        self._obj = obj

    # Delegate attribute lookup to internal obj
    def __getattr__(self, name):
        print('getattr:', name)
        return getattr(self._obj, name)

    # Delegate attribute assignment
    def __setattr__(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name, value)
        else:
            print('setattr:', name, value)
            setattr(self._obj, name, value)

    # Delegate attribute deletion
    def __delattr__(self, name):
        if name.startswith('_'):
            super().__delattr__(name)
        else:
            print('delattr:', name)
            delattr(self._obj, name)


class Spam:
    def __init__(self, x):
        self.x = x

    def bar(self, y):
        print('Spam.bar:', self.x, y)


class A3:
    def spam(self, x):
        print('A.spam', x)

    def foo(self):
        print('A.foo')


class B3(A3):
    def spam(self, x):
        print('B.spam')
        super().spam(x)

    def bar(self):
        print('B.bar')


class A4:
    def spam(self, x):
        print('A.spam', x)

    def foo(self):
        print('A.foo')


class B4:
    def __init__(self):
        self._a = A4()

    def spam(self, x):
        print('B.spam', x)
        self._a.spam(x)

    def bar(self):
        print('B.bar')

    def __getattr__(self, name):
        return getattr(self._a, name)
