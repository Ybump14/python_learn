'''4.15 顺序迭代合并后的排序迭代对象
问题:
你有一系列排序序列，想将它们合并后得到一个排序序列并在上面迭代遍历。

解决方案:
heapq.merge() 函数可以帮你解决这个问题。
heapq.merge 可迭代特性意味着它不会立马读取所有序列。
这就意味着你可以在非常长的序列中使用它，而不会有太大的开销。'''

import heapq

a = [1, 4, 7, 10]
b = [5, 1, 6, 11]

for c in heapq.merge(b, a, reverse=False):
    print(c, end=' ')  # 1 4 5 1 6 7 10 11

print('\n')

for c in heapq.merge(a, b, reverse=False):
    print(c, end=' ')  # 1 4 5 1 6 7 10 11

with open('E:\python_learn/python_cookbook/chapterData/python.csv', 'rt') as file1, \
        open('E:\python_learn/python_cookbook/chapterData/python_test.csv', 'rt') as file2, \
        open('E:\python_learn/python_cookbook/chapterData/merged_file.csv', 'wt', encoding='utf-8') as outf:
    for line in heapq.merge(file1, file2):
        outf.write(line)
