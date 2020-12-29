'''7.4 返回多个值的函数
问题:
你希望构造一个可以返回多个值的函数

解决方案:
为了能返回多个值，函数直接return一个元组就行了

讨论:
尽管myfun()看上去返回了多个值，实际上是先创建了一个元组然后返回的。
这个语法看上去比较奇怪，实际上我们使用的是逗号来生成一个元组，而不是用括号'''


def fun():
    return 1, 2, 3


a, b, c = fun()
print(a, b, c)

