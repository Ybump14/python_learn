'''4.2 代理迭代
问题:
你构建了一个自定义容器对象，里面包含有列表、元组或其他可迭代对象。
你想直接在你的这个新容器对象上执行迭代操作。

解决方案:
实际上你只需要定义一个 __iter__() 方法，将迭代操作代理到容器内部的对象上去。'''


class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)


# Example
if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)

    i = iter(root)
    try:
        while True:
            print(i.__next__())  # Node(1),Node(2)
    except StopIteration:
        print(format('Dividing', '*^20'))

    root._children.append('Node(3)')

    i = iter(root)
    try:
        while True:
            print(next(i))  # Node(1),Node(2),Node(3)
    except StopIteration:
        print(format('Dividing', '*^20'))

    root._children.append('JoJo')
    i = root.__iter__()
    try:
        while True:
            print(next(i))  # Node(1),Node(2),Node(3)
    except StopIteration:
        pass
