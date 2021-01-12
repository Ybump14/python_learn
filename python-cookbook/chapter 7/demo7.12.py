'''7.12 访问闭包中定义的变量
问题:
你想要扩展函数中的某个闭包，允许它能访问和修改函数的内部变量。

解决方案:
通常来讲，闭包的内部变量对于外界来讲是完全隐藏的。
但是，你可以通过编写访问函数并将其作为函数属性绑定到闭包上来实现这个目的。例如：'''


def sample():
    n = 0

    # Closure function
    def func():
        print('n=', n)

    # Accessor methods for n
    def get_n():
        return n

    def set_n(value):
        nonlocal n
        n = value

    # Attach as function attributes
    func.get_n = get_n
    func.set_n = set_n
    return func




class sam():
    def __init__(self, n, m):
        self.n = n
        self.m = m

    def set_n(self, n):
        self.n = n

    def get_n(self):
        print(self.n)


a = sam(1, 7)
a.set_n(12)
a.get_n()


