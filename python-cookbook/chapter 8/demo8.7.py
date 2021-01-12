'''8.7 调用父类方法
问题:
你想在子类中调用父类的某个已经被覆盖的方法。

解决方案:
为了调用父类(超类)的一个方法，可以使用 super() 函数'''


class A:
    def spam(self):
        return ('A.spam')

    def test(self):
        return ('A.test')


class B(A):
    def spam(self):
        return ('B.spam')

    def bb(self):
        super().spam()


b = B()
b.spam()  # B.spam
b.test()  # A.test
b.bb()  # A.spam


class C:
    def __init__(self):
        self.x = 0

    def get_x(self):
        return self.x


class D(C):
    def __init__(self):
        super().__init__()
        self.y = 1


d = D()
print(d.x)
print(d.y)


class Proxy:
    def __init__(self, obj):
        self._obj = obj

    # Delegate attribute lookup to internal obj
    def __getattr__(self, name):
        return getattr(self._obj, name)

    # Delegate attribute assignment
    def __setattr__(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name, value)  # Call original __setattr__
        else:
            setattr(self._obj, name, value)
