'''7.6 定义匿名或内联函数
问题:
你想为 sort() 操作创建一个很短的回调函数，但又不想用 def 去写一个单行函数，
而是希望通过某个快捷方式以内联方式来创建这个函数。

解决方案:
当一些函数很简单，仅仅只是计算一个表达式的值的时候，就可以使用lambda表达式来代替了'''

add = lambda x, y: x + y
print(add(1, 2))
print(add('Hello', 'World'))


# 这里使用的lambda表达式跟下面的效果是一样的：
def add(x, y):
    return x + y


names = ['David Beazley', 'Brian Jones',
         'Raymond Hettinger', 'Ned Batchelder']
print(sorted(names, key=lambda name: name.split()[-1].lower()))
