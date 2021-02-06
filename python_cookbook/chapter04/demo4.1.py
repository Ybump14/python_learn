'''4.1 手动遍历迭代器
问题:
你想遍历一个可迭代对象中的所有元素，但是却不想使用for循环。

解决方案:
为了手动的遍历可迭代对象，使用 next() 函数并在代码中捕获 StopIteration 异常。
比如，下面的例子手动读取一个文件中的所有行'''


def manual_iter():
    with open('E:\python_learn/python_cookbook/chapterData/python.csv') as f:
        try:
            while True:
                line = next(f)
                print(line, end='')
        except StopIteration:
            pass


def manual_iter_other():
    with open('E:\python_learn/python_cookbook/chapterData/python.csv') as f:
        while True:
            line = next(f, None)
            if line is None:
                break
            print(line, end='')


items = [1, 2, 3]
it = iter(items)
print(format(next(it), '^22'))  # Outputs 1
print(format(next(it), '^22'))  # Outputs 2
print(format(next(it), '^22'))  # Outputs 3
# print(format(next(it), '^22'))  # StopIteration
print(format('分割线', '*^20'))

items = [1, 2, 3]
it = iter(items)
print(format(it.__next__(), '^22'))  # Outputs 1
print(format(it.__next__(), '^22'))  # Outputs 2
print(format(it.__next__(), '^22'))  # Outputs 3
# print(format(it.__next__(), '^22'))  # StopIteration
