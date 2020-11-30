'''1.3 保留最后 N 个元素

问题:
在迭代操作或者其他操作的时候，怎样只保留最后有限几个元素的历史记录？

解决方案:
保留有限历史记录正是 collections.deque 大显身手的时候。
'''
from collections import deque

q = deque(maxlen=3)  # 新建一个固定大小为3的队列
q.append(1)
q.append(2)
q.append(3)
print(q)  # deque([1, 2, 3], maxlen=3)
q.append(4)  # 当新的元素加入并且这个队列已满的时候， 最老的元素会自动被移除掉。
print(q)  # deque([2, 3, 4], maxlen=3)

p = deque()  # 一个无限大小队列
p.append(1)
p.append(2)
p.append(3)
print(p)  # deque([1, 2, 3])
p.appendleft(4)
print(p)  # deque([4, 1, 2, 3])
print(p.pop())  # 弹出末位：3
print(p.popleft())  # 弹出首位：4
print(p)  # deque([1, 2])
