'''使用 new 关键字实现单例模式'''


class Single(object):
    _instance = None

    def __new__(cls, *args, **kw):
        if cls._instance is None:
            cls._instance = object.__new__(cls, *args, **kw)
        return cls._instance

    def __init__(self):
        pass


single1 = Single()
single2 = Single()
print(id(single1) == id(single2))
