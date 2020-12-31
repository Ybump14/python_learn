'''7.10 带额外状态信息的回调函数
问题:
你的代码中需要依赖到回调函数的使用(比如事件处理器、等待后台任务完成后的回调等)，
并且你还需要让回调函数拥有额外的状态值，以便在它的内部使用到。

解决方案:
这一小节主要讨论的是那些出现在很多函数库和框架中的回调函数的使用——特别是跟异步处理有关的。
为了演示与测试，我们先定义如下一个需要调用回调函数的函数：'''


def apply_async(func, args, *, callback):
    # Compute the result
    result = func(*args)

    # Invoke the callback with the result
    callback(result)


def print_result(result):
    print('Got:', result)


def add(x, y):
    return x + y


apply_async(add, ('Hello ', 'World'), callback=print_result)  # Got: Hello World


class ResultHandler:

    def __init__(self):
        self.sequence = 0

    def handler(self, result):
        self.sequence += 1
        print('[{}] Got: {}'.format(self.sequence, result))


r = ResultHandler()
apply_async(add, (2, 3), callback=r.handler)  # [1] Got: 5
apply_async(add, ('hello', 'world'), callback=r.handler)  # [2] Got: helloworld


def make_handler_off():
    sequence = 0

    def handler(result):
        nonlocal sequence
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))

    return handler


handler_off = make_handler_off()
apply_async(add, (2, 3), callback=handler_off)  # [1] Got: 5
apply_async(add, ('hello', 'world'), callback=handler_off)  # [2] Got: helloworld


def make_handler():
    sequence = 0
    while True:
        result = yield
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))


handler = make_handler()
handler.__next__()
apply_async(add, (2, 3), callback=handler.send)  # [1] Got: 5
apply_async(add, ('hello', 'world'), callback=handler.send)  # [2] Got: helloworld
