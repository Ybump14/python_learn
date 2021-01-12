'''4.5 反向迭代
问题:
你想反方向迭代一个序列

解决方案:
使用内置的 reversed() 函数
'''

a = [1, 2, 3, 4]
# for i in reversed(a):
# print(i)  # 4 3 2 1

# 反向迭代仅仅当对象的大小可预先确定或者对象实现了 __reversed__() 的特殊方法时才能生效。
# 如果两者都不符合，那你必须先将对象转换为一个列表才行
with open('E:\python_learn/python-cookbook/chapterData/python.csv') as f:
    print([line for line in f])


# with open('E:\python_learn/python-cookbook/chapterData/python.csv') as f:
#     for line in reversed((f)):  # TypeError： _io.TextIOWrapper
#         print(line, end='')

class Countdown:
    def __init__(self, start):
        self.start = start

    # Forward iterator
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    # Reverse iterator
    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1


for i in Countdown(9):
    print(format(i, '^2'), end='')  # 9 8 7 6 5 4 3 2 1
print('\n')

for i in reversed(Countdown(9)):
    print(format(i, '^2'), end='')  # 1 2 3 4 5 6 7 8 9
print('\n')


class List:
    def __init__(self, start):
        self.start = start

    # Forward iterator
    def __iter__(self):
        n = self.start
        i = 0
        while i < len(n):
            yield n[i]
            i += 1

    # Reverse iterator
    def __reversed__(self):
        n = self.start
        i = len(n) - 1
        while i >= 0:
            yield n[i]
            i -= 1


start = [1, 2, 3, 4, 5]
for i in List(start):
    print(format(i, '^2'), end='')  # 1 2 3 4 5
print('\n')
for i in reversed(List(start)):
    print(format(i, '^2'), end='')  # 5 4 3 2 1
