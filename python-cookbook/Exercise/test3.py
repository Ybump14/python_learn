import calendar
import time
from datetime import datetime, timedelta


class DateUtil:

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __repr__(self):
        return str(datetime(year=self.year, month=self.month, day=self.day))

    def dayStamp(self):
        stamp = datetime(year=self.year, month=self.month, day=self.day)
        sstamp = int(time.mktime(
            time.strptime(str(stamp.replace(hour=0, minute=0, second=0)), "%Y-%m-%d %H:%M:%S"))) * 1000
        estamp = int(time.mktime(time.strptime(str(stamp.replace(hour=23, minute=59, second=59)),
                                               "%Y-%m-%d %H:%M:%S"))) * 1000
        return sstamp, estamp

    def monthStamp(slef):
        firstDayWeekDay, monthRange = calendar.monthrange(slef.year, slef.month)
        firstDay = datetime(year=slef.year, month=slef.month, day=1)
        lastDay = datetime(year=firstDay.year, month=firstDay.month, day=monthRange)
        firstDay = int(time.mktime(time.strptime(str(firstDay), "%Y-%m-%d %H:%M:%S"))) * 1000
        lastDay = int(time.mktime(
            time.strptime(str(lastDay.replace(hour=23, minute=59, second=59)), "%Y-%m-%d %H:%M:%S"))) * 1000
        return firstDay, lastDay

    @classmethod
    def dayFirstStamp(cls):
        stamp = int(time.mktime(
            time.strptime(str(datetime.fromtimestamp(round(time.time())).replace(hour=0, minute=0, second=0)),
                          "%Y-%m-%d %H:%M:%S"))) * 1000
        return stamp

    @classmethod
    def dayLastStamp(cls):
        stamp = int(time.mktime(
            time.strptime(str(datetime.fromtimestamp(round(time.time())).replace(hour=23, minute=59, second=59)),
                          "%Y-%m-%d %H:%M:%S"))) * 1000
        return stamp

    @classmethod
    def monthFirstStamp(cls):
        stamp = datetime(year=datetime.now().year, month=datetime.now().month, day=1)
        stamp = int(time.mktime(time.strptime(str(stamp), "%Y-%m-%d %H:%M:%S"))) * 1000
        return stamp

    @classmethod
    def monthLastStamp(cls):
        firstDayWeekDay, monthRange = calendar.monthrange(datetime.now().year, datetime.now().month)
        stamp = datetime(year=datetime.now().year, month=datetime.now().month, day=monthRange)
        stamp = int(time.mktime(
            time.strptime(str(stamp.replace(hour=23, minute=59, second=59)), "%Y-%m-%d %H:%M:%S"))) * 1000
        return stamp

    @classmethod
    def lastMonthFirstStamp(cls):
        stamp = datetime(year=datetime.now().year, month=datetime.now().month, day=1) - timedelta(days=1)
        stamp = datetime(year=stamp.year, month=stamp.month, day=1)
        stamp = int(time.mktime(time.strptime(str(stamp), "%Y-%m-%d %H:%M:%S"))) * 1000
        return stamp

    @classmethod
    def lastMonthLastStamp(cls):
        stamp = datetime(year=datetime.now().year, month=datetime.now().month, day=1) - timedelta(days=1)
        stamp = int(time.mktime(
            time.strptime(str(stamp.replace(hour=23, minute=59, second=59)), "%Y-%m-%d %H:%M:%S"))) * 1000
        return stamp
