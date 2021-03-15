'''8.14 实现自定义容器
问题:
你想实现一个自定义的类来模拟内置的容器类功能，比如列表和字典。
但是你不确定到底要实现哪些方法。

解决方案:
collections 定义了很多抽象基类，当你想自定义容器类的时候它们会非常有用。
比如你想让你的类支持迭代，那就让你的类继承 collections.Iterable 即可：
'''
import bisect
from collections.abc import Sequence, MutableSequence


class SortedItems(Sequence):
    def __init__(self, initial=None):
        self._items = sorted(initial) if initial is not None else []

    # Required sequence methods
    def __getitem__(self, index):
        return self._items[index]

    def __len__(self):
        return len(self._items)

    # Method for adding an item in the right location
    def add(self, item):
        bisect.insort(self._items, item)


items = SortedItems([5, 1, 3])
print(list(items))
print(items[0], items[-1])
items.add(2)
print(list(items))


class Items(MutableSequence):
    def __init__(self, initial=None):
        self._items = list(initial) if initial is not None else []

    # Required sequence methods
    def __getitem__(self, index):
        print('Getting:', index)
        return self._items[index]

    def __setitem__(self, index, value):
        print('Setting:', index, value)
        self._items[index] = value

    def __delitem__(self, index):
        print('Deleting:', index)
        del self._items[index]

    def insert(self, index, value):
        print('Inserting:', index, value)
        self._items.insert(index, value)

    def __len__(self):
        print('Len')
        return len(self._items)
