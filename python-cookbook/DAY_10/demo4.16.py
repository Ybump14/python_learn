'''4.16 迭代器代替while无限循环
问题:
你在代码中使用 while 循环来迭代处理数据，
因为它需要调用某个函数或者和一般迭代模式不同的测试条件。
能不能用迭代器来重写这个循环呢？

解决方案:
一个常见的IO操作程序可能会想下面这样：'''

CHUNKSIZE = 8192

def reader(s):
    while True:
        data = s.recv(CHUNKSIZE)
        if data == b'':
            break
        process_data(data)

def reader2(s):
    for chunk in iter(lambda: s.recv(CHUNKSIZE), b''):
        pass
        # process_data(data)
