'''7.1 可接受任意数量参数的函数
问题:
你想构造一个可接受任意数量参数的函数。

解决方案:
为了能让一个函数接受任意数量的位置参数，可以使用一个*参数。
为了接受任意数量的关键字参数，使用一个以**开头的参数。'''

import html


def avg(first, *rest):
    return (first + sum(rest)) / (1 + len(rest))


# Sample use
avg(1, 2)  # 1.5
avg(1, 2, 3, 4)  # 2.5


def make_element(name, value, **attrs):
    keyvals = [' %s="%s"' % item for item in attrs.items()]
    attr_str = ''.join(keyvals)
    element = '<{name}{attrs}>{value}</{name}>'.format(
        name=name,
        attrs=attr_str,
        value=html.escape(value))
    return element


# Example
# Creates '<item size="large" quantity="6">Albatross</item>'
make_element('item', 'Albatross', size='large', quantity=6)

# Creates '<p>&lt;spam&gt;</p>'
make_element('p', '<spam>')


def anyargs(*args, **kwargs):
    print(args)  # A tuple
    print(kwargs)  # A dict


anyargs(1, 2, 3, a=1, b=2)

# (1, 2, 3)
# {'a': 1, 'b': 2}
