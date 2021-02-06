'''8.3 让对象支持上下文管理协议
问题:
你想让你的对象支持上下文管理协议(with语句)。

解决方案:
为了让一个对象兼容 with 语句，你需要实现 __enter__() 和 __exit__() 方法。
例如，考虑如下的一个类，它能为我们创建一个网络连接：

讨论:
编写上下文管理器的主要原理是你的代码会放到 with 语句块中执行。
当出现 with 语句的时候，对象的 __enter__() 方法被触发， 它返回的值(如果有的话)会被赋值给 as 声明的变量。
然后，with 语句块里面的代码开始执行。
最后，__exit__() 方法被触发进行清理工作。
'''

from socket import socket, AF_INET, SOCK_STREAM
from functools import partial


class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.sock = None

    def __enter__(self):
        if self.sock is not None:
            raise RuntimeError('Already connected')
        self.sock = socket(self.family, self.type)
        self.sock.connect(self.address)
        return self.sock

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.sock.close()
        self.sock = None


conn = LazyConnection(('www.baidu.com', 80))
with conn as s:
    s.send(b'GET /index.html HTTP/1.0\r\n')
    s.send(b'Host: www.baidu.com\r\n')
    s.send(b'\r\n')
    resp = b''.join(iter(partial(s.recv, 8192), b''))
