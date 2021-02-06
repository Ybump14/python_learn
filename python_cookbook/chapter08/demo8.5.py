'''8.5 在类中封装属性名
问题:
你想封装类的实例上面的“私有”数据，但是Python语言并没有访问控制。

解决方案:
Python程序员不去依赖语言特性去封装数据，而是通过遵循一定的属性和方法命名规约来达到这个效果。
第一个约定是任何以单下划线_开头的名字都应该是内部实现。比如：'''


class A:
    def __init__(self):
        self._internal = 0  # An internal attribute
        self.public = 1  # A public attribute

    def public_method(self):
        '''
        A public method
        '''
        pass

    def _internal_method(self):
        pass


class B:
    def __init__(self):
        self.__private = 0
        self.__test0 = 'test0'
        self._test1 = 'test1'
        self.test2 = 'test2'

    def __private_method(self):
        pass

    def public_method(self):
        pass
        self.__private_method()


class C(B):
    def __init__(self):
        super().__init__()
        self.__private = 1

    def __private_method(self):
        pass


a = A()
a.student = 'student'
print(a.student)
