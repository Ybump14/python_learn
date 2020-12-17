'''3.14 计算当前月份的日期范围
问题
你的代码需要在当前月份中循环每一天，想找到一个计算这个日期范围的高效方法。

解决方案
在这样的日期上循环并需要事先构造一个包含所有日期的列表。 你可以先计算出开始日期和结束日期，
然后在你步进的时候使用 datetime.timedelta 对象递增这个日期变量即可'''

from datetime import datetime, date, timedelta
import calendar


def get_month_range(start_date=None):
    if start_date is None:
        start_date = date.today().replace(day=1)
    _, days_in_month = calendar.monthrange(start_date.year, start_date.month)
    end_date = start_date + timedelta(days=days_in_month)
    return (start_date, end_date)


def Output_everyDay(first_day, last_day):
    while first_day < last_day:
        print(first_day)
        first_day += a_day


def date_range(start, stop, step):
    while start < stop:
        yield start
        start += step


a_day = timedelta(days=1)
first_day, last_day = get_month_range(date(2021, 2, 28))
Output_everyDay(first_day, last_day)
print(format('分割线','*^20'))
print([d for d in list(date_range(date(2020, 1, 11), date(2020, 2, 28), timedelta(days=7)))])
print(format('分割线','*^20'))
for d in date_range(date(2020, 1, 11), date(2020, 2, 28), timedelta(days=7)):
    print(d)
