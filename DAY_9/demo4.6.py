'''4.6 带有外部状态的生成器函数
问题:
你想定义一个生成器函数，但是它会调用某个你想暴露给用户使用的外部状态值。

解决方案:
如果你想让你的生成器暴露外部状态给用户，
别忘了你可以简单的将它实现为一个类，
然后把生成器函数放到 __iter__() 方法中过去。'''

from collections import deque


class linehistory:
    def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)

    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()

with open('E:\python_learn/data/python.csv') as f:
    lines = linehistory(f)
    for line in lines:
        if 'python' in line:
            for lineno, hline in lines.history:
                print('{}:{}'.format(lineno, hline), end='')




