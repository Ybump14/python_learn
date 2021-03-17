'''super()
'''


class A:
    def __init__(self):
        self.n = 2

    def add(self, m):
        print('self is {0} @A.add'.format(self))
        self.n += m


class B(A):
    def __init__(self):
        self.n = 3

    def add(self, m):
        print('self is {0} @B.add'.format(self))
        super().add(m)
        self.n += 3


class C(A):

    def __init__(self):
        self.n = 4

    def add(self, m):
        print('self is {0} @C.add'.format(self))
        super().add(m)
        self.n += 4


class D(B, C):
    # [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]

    def __init__(self):
        self.n = 5

    def add(self, m):
        print('self is {0} @D.add'.format(self))
        super(D, self).add(m)
        self.n += 5


print(D.mro())
d = D()
d.add(2)
'''
self is <__main__.D object at 0x01698AB0> @D.add
self is <__main__.D object at 0x01698AB0> @B.add
self is <__main__.D object at 0x01698AB0> @C.add
self is <__main__.D object at 0x01698AB0> @A.add
19
'''
print(d.n)
