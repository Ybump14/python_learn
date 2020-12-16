'''3.13 计算上一个周五的日期
问题:
你需要一个通用方法来计算一周中某一天上一次出现的日期，例如上一个周五的日期。

解决方案:
Python的 datetime 模块中有工具函数和类可以帮助你执行这样的计算。
下面是对类似这样的问题的一个通用解决方案'''

"""
Topic: 最后的周五
Desc :
"""

from datetime import datetime, timedelta

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
            'Friday', 'Saturday', 'Sunday']

