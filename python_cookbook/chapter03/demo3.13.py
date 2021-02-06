'''3.13 计算上一个周五的日期
问题:
你需要一个通用方法来计算一周中某一天上一次出现的日期，例如上一个周五的日期。

解决方案:
Python的 datetime 模块中有工具函数和类可以帮助你执行这样的计算。
下面是对类似这样的问题的一个通用解决方案'''

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from dateutil.rrule import *

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
            'Friday', 'Saturday', 'Sunday']


def get_previous_byday(dayname, start_date=None):
    if start_date is None:
        start_date = datetime.today()
    day_num = start_date.weekday()
    day_num_target = weekdays.index(dayname)
    days_ago = (7 + day_num - day_num_target) % 7
    if days_ago == 0:
        days_ago = 7
    target_date = start_date - timedelta(days=days_ago)
    return target_date


print(datetime.today())  # 2020-12-17 Thursday.
print(get_previous_byday('Monday'))  # 2020-12-14 Monday.
print(get_previous_byday('Thursday'))  # 2020-12-10 Thursday.
print(format('分割线', '*^24s'))
d = datetime.now()  # 2020-12-17 Thursday

# 若今天是本周的TH,那么上一个TH就是今天
# 还未到本周的FR,那么上一个FR就是上一周的FR
# 以两组例子观察
print(d + relativedelta(weekday=MO(-1)))  # 2020-12-14
print(d + relativedelta(weekday=TU(-1)))  # 2020-12-17
print(d + relativedelta(weekday=WE(-1)))  # 2020-12-16
print(d + relativedelta(weekday=TH(-1)))  # 2020-12-17
print(d + relativedelta(weekday=FR(-1)))  # 2020-12-11
print(format('分割线', '*^24s'))
print(d + relativedelta(weekday=MO(-2)))  # 2020-12-07
print(d + relativedelta(weekday=TU(-2)))  # 2020-12-08
print(d + relativedelta(weekday=WE(-2)))  # 2020-12-09
print(d + relativedelta(weekday=TH(-2)))  # 2020-12-10
print(d + relativedelta(weekday=FR(-2)))  # 2020-12-04
