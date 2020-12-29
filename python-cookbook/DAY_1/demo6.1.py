'''6.1 读写CSV数据

问题:
你想读写一个CSV格式的文件。

解决方案:
对于大多数的CSV格式的数据读写问题，都可以使用 csv 库。
'''

import csv
from collections import namedtuple

'''以list迭代行内容'''
with open('E:\python_learn/python-cookbook/data/python.csv') as f:
    f_csv = csv.reader(f)
    header = next(f_csv)
    for row in f_csv:
        print(row[0], row[1], row[2], row[3])
    print('\n')

'''以tuple迭代行内容'''
with open('E:\python_learn/python-cookbook/data/python.csv') as f:
    f_csv = csv.reader(f)
    headings = next(f_csv)
    Row = namedtuple('Row', headings)
    for r in f_csv:
        row = Row(*r)
        print(row.file_name, row.request_method, row.request_api, row.request_name)
    print('\n')

'''以dict迭代行内容'''
with open('E:\python_learn/python-cookbook/data/python.csv') as f:
    dict_csv = csv.DictReader(f)
    for dict in dict_csv:
        print(dict['file_name'], dict['request_method'], dict['request_api'], dict['request_name'], sep=',')
