'''3.16 结合时区的日期操作
问题:
你有一个安排在2012年12月21日早上9:30的电话会议，地点在芝加哥。
而你的朋友在印度的班加罗尔，那么他应该在当地时间几点参加这个会议呢？

解决方案:
对几乎所有涉及到时区的问题，你都应该使用 pytz 模块。这个包提供了Olson时区数据库，
它是时区信息的事实上的标准，在很多语言和操作系统里面都可以找到'''

from datetime import datetime
from pytz import timezone

d = datetime(2012, 12, 21, 9, 30, 0)
print(d)

# Localize the date for Chicago
central = timezone('US/Central')
loc_d = central.localize(d)
print(loc_d)

# Convert to Bangalore time
bang_d = loc_d.astimezone(timezone('Asia/Kolkata'))
print(bang_d)



