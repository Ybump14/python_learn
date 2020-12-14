'''1.18 映射名称到序列元素
问题:
你有一段通过下标访问列表或者元组中元素的代码，但是这样有时候会使得你的代码难以阅读， 于是你想通过名称来访问元素。

解决方案:
collections.namedtuple() 函数通过使用一个普通的元组对象来帮你解决这个问题。
这个函数实际上是一个返回 Python 中标准元组类型子类的一个工厂方法。
你需要传递一个类型名和你需要的字段给它，然后它就会返回一个类，你可以初始化这个类，为你定义的字段传递值等'''
from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')

records_one = (1, 2, 3, 4, 5)
records_arg = ((1, 2, 3, 4, 5), (6, 7, 8, 9, 10))

Stock = namedtuple('Stock', ['one', 'two', 'three', 'four', 'five'])
s = Stock(*records_one)  # Stock(one=1, two=2, three=3, four=4, five=5)


def compute_cost(records):  # 普通元组的代码
    total = 0.0
    for rec in records:
        total += rec[1] * rec[2]  # (2*3)+(7*8)=6+56=62
    return total


def compute_cost_nametuple(records):  # 命名元组的版本
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.two * s.three  # (2*3)+(7*8)=6+56=62
    return total


Stock = namedtuple('Stock', ['name', 'share', 'price'])
s = Stock('ACME', 100, 123.45)  # Stock(name='ACME', share=100, price=123.45)

# 一个命名元组是不可更改的,如:
# s.share = 75  -> AttributeError: can't set attribut

# 命名元组实例的 _replace() 方法
s = s._replace(share=75)  # Stock(name='ACME', share=75, price=123.45)

Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
# Create a prototype instance
stock_prototype = Stock('', 0, 0.0, None, None)
a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}
c = (1, 2, 3, 4, 5)
d = [1, 2, 3, 4, 5]
e = {1, 2, 3, 4, 5}


# Function to convert a dictionary to a Stock
def dict_to_stock(s):
    return stock_prototype._replace(**s)


def nodict_to_stock(s):
    return stock_prototype._replace(name=s[0], shares=s[1], price=s[2], date=s[3], time=s[4])


def set_to_stock(s):
    i = []
    for values in s:
        i.append(values)
    return stock_prototype._replace(name=i[0], shares=i[1], price=i[2], date=i[3], time=i[4])


print(dict_to_stock(a))  # Stock(name='ACME', shares=100, price=123.45, date=None, time=None)
print(dict_to_stock(b))  # Stock(name='ACME', shares=100, price=123.45, date='12/17/2012', time=None)
print(nodict_to_stock(c))  # Stock(name=1, shares=2, price=3, date=4, time=5)
print(nodict_to_stock(d))  # Stock(name=1, shares=2, price=3, date=4, time=5)
print(set_to_stock(e))  # Stock(name=1, shares=2, price=3, date=4, time=5)
