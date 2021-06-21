'''使用 metaclass 实现单例模式'''


def func(self):
    print("do sth")


Klass = type("Klass", (), {"func": func})

c = Klass()
c.func()


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Cls4(metaclass=Singleton):
    pass


cls1 = Cls4()
cls2 = Cls4()
print(id(cls1) == id(cls2))
