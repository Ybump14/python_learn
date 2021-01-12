'''1.1 将序列分解为单独的变量

问题:
现在有一个包含 N 个元素的元组或者是序列，怎样将它里面的值解压后同时赋值给 N 个变量？

解决方案:
任何的序列（或者是可迭代对象）可以通过一个简单的赋值操作来分解为单独的变量。
唯一的要求就是变量的总数和结构必须与序列相吻合。

讨论:
不仅仅只是元组或列表，只要对象是可迭代的，就可以执行分解操作。
包括字符串，文件对象，迭代器和生成器.
'''

"list"
data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data

name, shares, price, (year, month, day) = data

"str"
data = "helloW"
one, two, three, four, five, six = data

"trup"
data = ("AAA", ("BBB", "CCC"))

"dict"
data = {"AAA": "aaa", "BBB": "bbb", "CCC": "ccc"}

a, b, c = data.keys()
a, b, c = data  # 默认迭代的是keys,等同a, b, c = chapterData.keys()
a, b, c = data.values()
(a, a1), (b, b1), (c, c1) = data.items()

p = (4, 5)
x, y, z = p
'''Traceback (most recent call last):
  File "E:/python_learn/chapter 1/demo1.1.py", line 19, in <module>
    x, y, z = p
ValueError: not enough values to unpack (expected 3, got 2)'''
