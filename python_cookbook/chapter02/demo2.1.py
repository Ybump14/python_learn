'''2.1 使用多个界定符分割字符串
问题:
你需要将一个字符串分割为多个字段，但是分隔符(还有周围的空格)并不是固定的。

解决方案:
string 对象的 split() 方法只适应于非常简单的字符串分割情形，
它并不允许有多个分隔符或者是分隔符周围不确定的空格。
当你需要更加灵活的切割字符串的时候，最好使用 re.split() 方法'''

import re

line = 'asdf fjdk; afed, fjek, asdf, foo'
print(line.split())
print(line.split("  "))
print(re.split(r'[,;\s]', line))
print(re.split(r'[,;\s]\s*', line))
print(re.split(r'(;|,|\s)\s*', line))  # 括号捕获分组
print(re.split(r'(?:;|,|\s)\s*', line))  # 非捕获分组,形如 (?:...)

fields = re.split(r'(;|,|\s)\s*', line)
values = fields[::2]
delimiters = fields[1::2] + ['']
print(''.join(v + d for v, d in zip(values, delimiters)))

# str.join(sequence)
str = "-"
seq = ("a", "b", "c")  # 字符串序列
print("".join(seq))  # Outputs a-b-c

data = "@1222_finishPeriodBorrowBalance+@1223_finishPeriodBorrowBalance+@1224_finishPeriodBorrowBalance"
bb = "@1222_finishPeriodBorrowBalance;@1223_finishPeriodBorrowBalance;@1224_finishPeriodBorrowBalance;"
sub = bb.split(';')
# print(sub)

for i in sub:
    a = i.split('_')
    if len(a) > 1:
        print(a[0].replace('@', ''),a[1])
