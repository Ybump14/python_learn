'''9.1 在函数上添加包装器
问题:
你想在函数上添加一个包装器，增加额外的操作处理 (比如日志、计时等)。

解决方案:
如果你想使用额外的代码包装一个函数，可以定义一个装饰器函数，例如'''

import time
from functools import wraps


def timethis(func):
    '''
    Decorator that reports the execution time.
    '''

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result

    return wrapper


@timethis
def countdown(n):
    '''
     Counts down
    '''
    while n > 0:
        n -= 1


countdown(100000)
