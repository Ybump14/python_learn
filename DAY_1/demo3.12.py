from datetime import datetime
import time

'''给定字符串20200601,计算是今年的第几天'''
# 简单实现
test_day = "20200601"
date = datetime(int(test_day[0:4]), int(test_day[4:6]), int(test_day[6:8]))
start = datetime(datetime.now().year, 1, 1)
n = (date - start).days + 1
print(n)

input_str = '20200601'
t = time.strptime(input_str, '%Y%m%d')
print(time.strftime('%j', t))
