'''6.1 读写CSV数据
问题:
你想读写一个CSV格式的文件。

解决方案:
对于大多数的CSV格式的数据读写问题，都可以使用 csv 库。
'''

import csv
from collections import namedtuple


def read_csv1():
    with open('stocks.csv') as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        for row in f_csv:
            print(row)


def read_csv2():
    with open('stocks.csv') as f:
        f_csv = csv.reader(f)
        headings = next(f_csv)
        Row = namedtuple('Row', headings)
        for r in f_csv:
            row = Row(*r)
            print(row)
            # print(row.Symbol, row.Price, row.Date, row.Time, row.Change, row.Volume)


read_csv1()
read_csv2()
