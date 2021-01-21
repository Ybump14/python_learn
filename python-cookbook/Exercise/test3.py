import time
from datetime import datetime


class DateUtil:

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def timeStamp(self):
        stamp = datetime(year=self.year, month=self.month, day=self.day)
        sstamp = int(time.mktime(
            time.strptime(str(stamp.replace(hour=0, minute=0, second=0)), "%Y-%m-%d %H:%M:%S"))) * 1000
        estamp = int(time.mktime(time.strptime(str(stamp.replace(hour=23, minute=59, second=59)),
                                               "%Y-%m-%d %H:%M:%S"))) * 1000
        return sstamp, estamp

    @classmethod
    def stamp(cls):
        sta = round(time.time())
        sstamp = int(time.mktime(time.strptime(str(datetime.fromtimestamp(sta).replace(hour=0, minute=0, second=0)),
                                               "%Y-%m-%d %H:%M:%S"))) * 1000
        estamp = int(time.mktime(time.strptime(str(datetime.fromtimestamp(sta).replace(hour=23, minute=59, second=59)),
                                               "%Y-%m-%d %H:%M:%S"))) * 1000
        return sstamp, estamp
