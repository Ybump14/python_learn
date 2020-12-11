'''1.10 删除序列相同元素并保持顺序
问题:
怎样在一个序列上面保持元素顺序的同时消除重复的值？

解决方案:
如果序列上的值都是 hashable 类型，那么可以很简单的利用集合或者生成器来解决这个问题。'''


def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item*item
            seen.add(item)

a = [1, 5, 2, 1, 9, 1, 5, 10]
print(list(dedupe(a)))
