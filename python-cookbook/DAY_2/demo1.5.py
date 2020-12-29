'''1.5 实现一个优先级队列

问题:
怎样实现一个按优先级排序的队列？ 并且在这个队列上面每次 pop 操作总是返回优先级最高的那个元素

解决方案:
利用 heapq 模块实现一个简单的优先级队列

讨论:
不仅仅只是元组或列表，只要对象是可迭代的，就可以执行分解操作。
包括字符串，文件对象，迭代器和生成器。

相关概念：
堆是非线性的树形的数据结构，有两种堆，最大堆与最小堆。（ heapq库中的堆默认是最小堆）
最大堆，树种各个父节点的值总是大于或等于任何一个子节点的值。
最小堆，树种各个父节点的值总是小于或等于任何一个子节点的值。
我们一般使用二叉堆来实现优先级队列,它的内部调整算法复杂度为logN。
堆是一个二叉树，其中最小堆每个父节点的值都小于或等于其所有子节点的值。
整个最小堆的最小元素总是位于二叉树的根节点。
python的heapq模块提供了对堆的支持。 heapq堆数据结构最重要的特征是heap[0]永远是最小的元素

'''

import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 2)
print(q._queue)
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
