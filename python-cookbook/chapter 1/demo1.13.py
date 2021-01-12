'''1.13 通过某个关键字排序一个字典列表
问题:
你有一个字典列表，你想根据某个或某几个字典字段来排序这个列表。

解决方案:
通过使用 operator 模块的 itemgetter 函数，可以非常容易的排序这样的数据结构。'''

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

from operator import itemgetter

rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))
print(rows_by_fname)
print(rows_by_uid)
rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))
print(rows_by_lfname)

rows_by_fname = sorted(rows, key=lambda r: r['fname'])
rows_by_lfname = sorted(rows, key=lambda r: (r['lname'], r['fname']))
print(rows_by_fname)
print(rows_by_uid)

min_rows_by_fname = min(rows, key=itemgetter('fname'))
max_rows_by_fname = max(rows, key=itemgetter('fname'))
min_rows_by_uid = min(rows, key=itemgetter('uid'))
max_rows_by_uid = max(rows, key=itemgetter('uid'))
print(min_rows_by_fname)
print(max_rows_by_fname)
print(min_rows_by_uid)
print(max_rows_by_uid)
