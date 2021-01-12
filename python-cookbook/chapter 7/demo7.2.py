'''7.2 只接受关键字参数的函数
问题:
你希望函数的某些参数强制使用关键字参数传递

解决方案:
将强制关键字参数放到某个*参数或者单个*后面就能达到这种效果。'''


def recv(maxsize, *, block):
    'Receives a message'
    pass


# recv(1024, True)  # TypeError
recv(1024, block=True)  # Ok


def minimum(*values, clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    print(m)


minimum(1, 5, 2, -5, 10)  # Returns -5
minimum(1, 5, 2, -5, 10, clip=0)  # Returns 0
