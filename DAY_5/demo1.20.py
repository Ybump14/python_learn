'''1.20 合并多个字典或映射
问题:
现在有多个字典或者映射，你想将它们从逻辑上合并为一个单一的映射后执行某些操作，
比如查找值或者检查某些键是否存在。

解决方案:
假如你有如下两个字典:
a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }
现在假设你必须在两个字典中执行查找操作（比如先从 a 中找，如果找不到再在 b 中找）。
一个非常简单的解决方案就是使用 collections 模块中的 ChainMap 类。'''

from collections import ChainMap

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
c = ChainMap(a, b)
print(c)  # Outputs ChainMap({'x': 1, 'z': 3}, {'y': 2, 'z': 4})
print(c['x'])  # Outputs 1 (from a)
print(c['y'])  # Outputs 2 (from b)
print(c['z'])  # Outputs 3 (from a)
print(len(c))  # Outputs 3
print(list(c.keys()))  # Outputs ['y', 'z', 'x']
print(list(c.values()))  # Outputs [2, 3, 1]

values = ChainMap()
values['x'] = 1
# print(values)  # Outputs ChainMap({'x': 1})
print(values['x'])  # Outputs 1
values = values.new_child()
# print(values)  # Outputs ChainMap({}, {'x': 1})
values['x'] = 2
print(values['x'])  # Outputs 2
# print(values)  # Outputs ChainMap({'x': 2}, {'x': 1})
values = values.new_child()
# print(values)  # Outputs ChainMap({}, {'x': 2}, {'x': 1})
values['x'] = 3
print(values['x'])  # Outputs 3
# print(values)  # Outputs ChainMap({'x': 3}, {'x': 2}, {'x': 1})
values['x'] = 4
print(values['x'])  # Outputs 4
# print(values)  # Outputs ChainMap({'x': 4}, {'x': 2}, {'x': 1})
values = values.parents
print(values['x'])  # Outputs 2
print(values)  # Outputs ChainMap({'x': 2}, {'x': 1})
values = values.parents
print(values['x'])  # Outputs 1
print(values)  # Outputs ChainMap({'x': 1})
