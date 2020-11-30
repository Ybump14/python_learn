'''1.2 解压可迭代对象赋值给多个变量

问题:
如果一个可迭代对象的元素个数超过变量个数时，会抛出一个 ValueError 。
那么怎样才能从这个可迭代对象中解压出 N 个元素出来？

解决方案:
Python的星号表达式可以用来解决这个问题。
'''

record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, mail, *telephone = record
'''Dave
'dave@example.com'
['773-555-1212','847-555-1212']
'''

name, *mail, telephone = record
'''Dave
['dave@example.com','773-555-1212']
847-555-1212'''

name, *mail, a, b = record
'''Dave
['dave@example.com']
773-555-1212
847-555-1212'''

name, mail, *telephone, a, b = record
'''Dave
'dave@example.com'
[]
773-555-1212
847-555-1212'''

name, mail, *telephone, a, b, c = record
'''ValueError: not enough values to unpack (expected at least 5, got 4)'''

*name, mail, *telephone, a = record
'''SyntaxError: two starred expressions in assignment'''

line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
'''nobody
['*', '-2', '-2', 'Unprivileged User']
/var/empty
/usr/bin/false'''
