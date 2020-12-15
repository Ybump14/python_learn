'''2.3 用Shell通配符匹配字符串
问题:
你想使用 Unix Shell 中常用的通配符(比如 *.py , Dat[0-9]*.csv 等)去匹配文本字符串

解决方案:
fnmatch 模块提供了两个函数—— fnmatch() 和 fnmatchcase() ，可以用来实现这样的匹配
fnmatch() 函数使用底层操作系统的大小写敏感规则
fnmatchcase() 完全使用你的模式大小写匹配'''

from fnmatch import fnmatch, fnmatchcase

fnmatch('foo.txt', '*.txt')  # 'True'
fnmatch('foo.txt', '?oo.txt')  # 'True'
fnmatch('Dat45.csv', 'Dat[0-9]*')  # 'True'
names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
print([name for name in names if fnmatch(name, 'Dat*.csv')])  # ['Dat1.csv', 'Dat2.csv']

addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
]
print([addr for addr in addresses if
       fnmatchcase(addr, '* ST')])  # ['5412 N CLARK ST', '1060 W ADDISON ST', '2122 N CLARK ST']
print([addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9] *CLARK*')])  # ['5412 N CLARK ST']

dict_abc = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

print([value for key, value in dict_abc.items() if fnmatchcase(key, '*A*')])  # 大小写敏感
print([value for key, value in dict_abc.items() if fnmatch(key, '*a*')])  # Windows下大小写不敏感
