'''4.12 不同集合上元素的迭代
问题:
你想在多个对象执行相同的操作，但是这些对象在不同的容器中，你希望代码在不失可读性的情况下避免写重复的循环。

解决方案:
itertools.chain() 方法可以用来简化这个任务。
它接受一个可迭代对象列表作为输入，并返回一个迭代器，有效的屏蔽掉在多个容器中迭代细节。'''

from itertools import chain

a = [1, 2, 3, 4]
b = ['x', 'y', 'z']
c = (10, 11, 12)
d = {'set1', 'set2'}
e = {'a_key': 'a_value', 'b_key': 'b_value'}
print(list(chain(a, b, c, d, e)))  # [1, 2, 3, 4, 'x', 'y', 'z', 10, 11, 12, 'set1', 'set2', 'akey', 'bkey']
print(list(chain(a, b, c, d, e.items())))  # [1, 2, 3, 4, 'x', 'y', 'z', 10, 11, 12, 'set2', 'set1', ('a_key', 'a_value'), ('b_key', 'b_value')]

# 使用 chain() 的一个常见场景是当你想对不同的集合中所有元素执行某些操作的时候。比如：
active_items = set()
inactive_items = set()

# Iterate over all items
for item in chain(active_items, inactive_items):
    # Process item
    ...

# 这种解决方案要比像下面这样使用两个单独的循环更加优雅，
for item in active_items:
    # Process item
    ...

for item in inactive_items:
    # Process item
    ...
