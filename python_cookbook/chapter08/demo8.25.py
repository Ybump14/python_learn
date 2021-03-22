'''8.25 创建缓存实例
问题
在创建一个类的对象时，如果之前使用同样参数创建过这个对象， 你想返回它的缓存引用。

解决方案
这种通常是因为你希望相同参数创建的对象时单例的。
在很多库中都有实际的例子，比如 logging 模块，使用相同的名称创建的 logger 实例永远只有一个。例如：'''


# The class in question
class Spam:
    def __init__(self, name):
        self.name = name


# Caching support
import weakref

_spam_cache = weakref.WeakValueDictionary()


def get_spam(name):
    if name not in _spam_cache:
        s = Spam(name)
        _spam_cache[name] = s
    else:
        s = _spam_cache[name]
    return s
