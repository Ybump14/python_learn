'''1.6 字典中的键映射多个值
问题:
怎样实现一个键对应多个值的字典（也叫 multidict）？

解决方案:
一个字典就是一个键对应一个单值的映射。如果你想要一个键映射多个值，
那么你就需要将这多个值放到另外的容器中， 比如列表或者集合里面。
比如，你可以像下面这样构造这样的字典：'''

from collections import defaultdict

d = {}
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('b', []).append(4)
d.setdefault('b', []).append(4)

d = {}
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('b', []).append(4)
d.setdefault('b', []).append(4)

d = {}
d.setdefault('a', {})['b'] = 1
d.setdefault('a', {})['c'] = 2
d.setdefault('a', {})['d'] = 4
d.setdefault('a', {})['d'] = 4

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
d['b'].append(4)

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)
d['b'].add(4)

d = defaultdict(dict)
d['a']['b'] = 1
d['a']['c'] = 2
d['a']['d'] = 4
d['a']['d'] = 4
