'''8.17 创建不调用init方法的实例
问题:
你想创建一个实例，但是希望绕过执行 __init__() 方法。

解决方案:
可以通过 __new__() 方法创建一个未初始化的实例。'''

from time import localtime


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def today(cls):
        d = cls.__new__(cls)
        t = localtime()
        d.year = t.tm_year
        d.month = t.tm_mon
        d.day = t.tm_mday
        return d

    def get_today(self):
        return self.year, self.month, self.day


print(Date.today().get_today())
