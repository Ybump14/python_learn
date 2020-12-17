'''3.15 字符串转换为日期
问题:
你的应用程序接受字符串格式的输入，但是你想将它们转换为 datetime 对象以便在上面执行非字符串操作。

解决方案:
使用Python的标准模块 datetime 可以很容易的解决这个问题'''

from datetime import datetime

text = '2012-09-20'
y = datetime.strptime(text, '%Y-%m-%d')
z = datetime.now()
diff = z - y
print(diff)
print(y)
print(z)
