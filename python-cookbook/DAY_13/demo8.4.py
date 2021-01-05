'''8.4 创建大量对象时节省内存方法
问题:
你的程序要创建大量(可能上百万)的对象，导致占用很大的内存。

解决方案:
对于主要是用来当成简单的数据结构的类而言，你可以通过给类添加 __slots__ 属性来极大的减少实例所占的内存。

讨论:
关于 __slots__ 的一个常见误区是它可以作为一个封装工具来防止用户给实例增加新的属性。
尽管使用slots可以达到这样的目的，
但是这个并不是它的初衷。 __slots__ 更多的是用来作为一个内存优化工具'''


class Date:
    __slots__ = ['year', 'month', 'day']

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day



