import calendar
import time
from datetime import datetime, timedelta


class DateUtil:

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def DayStamp(self):
        stamp = datetime(year=self.year, month=self.month, day=self.day)
        sstamp = int(time.mktime(
            time.strptime(str(stamp.replace(hour=0, minute=0, second=0)), "%Y-%m-%d %H:%M:%S"))) * 1000
        estamp = int(time.mktime(time.strptime(str(stamp.replace(hour=23, minute=59, second=59)),
                                               "%Y-%m-%d %H:%M:%S"))) * 1000
        return sstamp, estamp

    def Month_Stamp(slef):
        firstDayWeekDay, monthRange = calendar.monthrange(slef.year, slef.month)
        firstDay = datetime(year=slef.year, month=slef.month, day=1)
        lastDay = datetime(year=firstDay.year, month=firstDay.month, day=monthRange)
        firstDay = int(time.mktime(time.strptime(str(firstDay), "%Y-%m-%d %H:%M:%S"))) * 1000
        lastDay = int(time.mktime(
            time.strptime(str(lastDay.replace(hour=23, minute=59, second=59)), "%Y-%m-%d %H:%M:%S"))) * 1000
        return firstDay, lastDay

    @classmethod
    def thisDayStamp(cls):
        sstamp = int(time.mktime(
            time.strptime(str(datetime.fromtimestamp(round(time.time())).replace(hour=0, minute=0, second=0)),
                          "%Y-%m-%d %H:%M:%S"))) * 1000
        estamp = int(time.mktime(
            time.strptime(str(datetime.fromtimestamp(round(time.time())).replace(hour=23, minute=59, second=59)),
                          "%Y-%m-%d %H:%M:%S"))) * 1000
        return sstamp, estamp

    @classmethod
    def thisMonthStamp(cls):
        firstDayWeekDay, monthRange = calendar.monthrange(datetime.now().year, datetime.now().month)
        thisMonth_firstDay = datetime(year=datetime.now().year, month=datetime.now().month, day=1)
        thisMonth_lastDay = datetime(year=datetime.now().year, month=datetime.now().month, day=monthRange)
        thisMonth_firstDay = int(time.mktime(time.strptime(str(thisMonth_firstDay), "%Y-%m-%d %H:%M:%S"))) * 1000
        thisMonth_lastDay = int(time.mktime(
            time.strptime(str(thisMonth_lastDay.replace(hour=23, minute=59, second=59)), "%Y-%m-%d %H:%M:%S"))) * 1000
        return thisMonth_firstDay, thisMonth_lastDay

    @classmethod
    def lastMonthStamp(cls):
        lastMonth_lastDay = datetime(year=datetime.now().year, month=datetime.now().month, day=1) - timedelta(days=1)
        lastMonth_firstDay = datetime(year=lastMonth_lastDay.year, month=lastMonth_lastDay.month, day=1)
        lastMonth_firstDay = int(time.mktime(time.strptime(str(lastMonth_firstDay), "%Y-%m-%d %H:%M:%S"))) * 1000
        lastMonth_lastDay = int(time.mktime(
            time.strptime(str(lastMonth_lastDay.replace(hour=23, minute=59, second=59)), "%Y-%m-%d %H:%M:%S"))) * 1000
        return lastMonth_firstDay, lastMonth_lastDay


print(DateUtil.thisMonthStamp()[0])
print(DateUtil.thisMonthStamp()[1])
print(DateUtil.lastMonthStamp()[0])
print(DateUtil.lastMonthStamp()[1])

print(DateUtil(2020, 2, 2).Month_Stamp()[0])
print(DateUtil(2020, 2, 2).Month_Stamp()[1])
