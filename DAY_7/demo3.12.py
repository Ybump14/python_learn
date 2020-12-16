'''3.12 基本的日期与时间转换
问题:
你需要执行简单的时间转换，比如天到秒，小时到分钟等的转换。

解决方案:
为了执行不同时间单位的转换和计算，请使用 datetime 模块。'''

from datetime import timedelta
from datetime import datetime

a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)
c = a + b
print(c)  # 2 days, 10:30:00
print(c.days)  # 2
print(c.seconds)  # 37800
print(c.seconds / 3600)  # 10.5
print(c.total_seconds() / 3600)  # 58.5

# datetime 的实例使用标准的数学运算
a = datetime(2012, 9, 23)
print(a)
print(a + timedelta(days=10, hours=6, seconds=60, minutes=5, weeks=1))
b = datetime(2012, 12, 21)
c = b - a
print(c)
now = datetime.now()
print(now)
print(now + timedelta(minutes=5))

# datetime 会自动处理闰年。比如:
a = datetime(2012, 3, 1)
b = datetime(2012, 2, 28)
print(a - b)
print((a - b).days)
c = datetime(2013, 3, 1)
d = datetime(2013, 2, 28)
print((c - d).days)


