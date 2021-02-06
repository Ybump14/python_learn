from datetime import datetime
import time

'''给定字符串20200601,计算是今年的第几天'''
# 简单实现
test_day = "20200601"
date = datetime(int(test_day[0:4]), int(test_day[4:6]), int(test_day[6:8]))
start = datetime(date.year, 1, 1)
n = (date - start).days + 1
print(n)

# 时间戳 转化 为 时间元组 time.gmtime()
# 字符串 转化 为 时间元组 time.strptime(t, '%Y%m%d')

# 时间元组 转化为 时间戳 time.mktime()
# 时间元组 转化为 字符串 time.strftime('%Y-%m-%d', t)

# 时间戳 转化为 datetime.datetime ,str转为字符串
# datetime.fromtimestamp(round(time.time()))

input_str = '20200601'
t_str = time.strptime(input_str, '%Y%m%d')
t_str1 = time.mktime(t_str)
print(t_str1)

input_time_tuple = round(time.time())
t_tuple = time.gmtime(input_time_tuple)
t_tuple1 = time.mktime(t_tuple)
print(t_tuple1)

t_str2 = time.strftime('%Y-%m-%d', t_str)
print(t_str2)

t_str3 = time.strftime('%Y-%m-%d %H:%M:%S', t_tuple)
print(t_str3)

print(time.strptime(str(datetime.fromtimestamp(round(time.time()))), '%Y-%m-%d %H:%M:%S'))

print(datetime.utcfromtimestamp(round(time.time())))

print(datetime.fromisoformat('2020-06-01'))

print(datetime(2020,2,2).timetuple())
