'''3.15 字符串转换为日期
问题:
你的应用程序接受字符串格式的输入，但是你想将它们转换为 datetime 对象以便在上面执行非字符串操作。

解决方案:
使用Python的标准模块 datetime 可以很容易的解决这个问题'''

from datetime import datetime
import time, timeit

text = '2012-09-20'
# strptime() 的性能较差,它是使用纯Python实现
print(datetime.strptime(text, '%Y-%m-%d'))
print(format('分割线', '*^17s'))


def parse_ymd(s):
    year_s, month_s, day_s = s.split('-')
    return datetime(int(year_s), int(month_s), int(day_s))


start = time.perf_counter()
print(start)
print(parse_ymd('2012-09-20'))
end = time.perf_counter()
print(end)
print('Running time is:%s Seconds' % (end - start))

print(format('分割线', '*^17s'))

start = time.perf_counter()
print(datetime.strptime('2012-09-20', '%Y-%m-%d'))
end = time.perf_counter()
print('Running time is:%s Seconds' % (end - start))
