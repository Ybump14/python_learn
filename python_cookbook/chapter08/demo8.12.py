'''8.12 定义接口或者抽象基类
问题:
你想定义一个接口或抽象类，并且通过执行类型检查来确保子类实现了某些特定的方法

解决方案:
使用 abc 模块可以很轻松的定义抽象基类'''

from abc import ABCMeta, abstractmethod


class IStream(metaclass=ABCMeta):
    @abstractmethod
    def read(self, maxbytes=-1):
        pass

    @abstractmethod
    def write(self, data):
        pass


# 抽象类的一个特点是它不能直接被实例化，比如你想像下面这样做是不行的：
# a = IStream()
# TypeError: Can't instantiate abstract class IStream with abstract methods read, write

# 抽象类的目的就是让别的类继承它并实现特定的抽象方法：
class SocketStream(IStream):
    def read(self, maxbytes=-1):
        pass

    def write(self, data):
        pass


class Database(metaclass=ABCMeta):
    def register(self, host, user, password):
        print("Host : {}".format(host))
        print("User : {}".format(user))
        print("Password : {}".format(password))
        print("Register Success!")

    @abstractmethod
    def query(self, *args):
        """
        传入查询数据的SQL语句并执行
        """

    @staticmethod
    @abstractmethod
    def execute(sql_string):
        """
        执行SQL语句
        """

    @abstractmethod
    def test(self):
        pass


# 抽象基类Database的实现可以看出，它共包含3个方法，
# register是每个子类都需要的，直接实现在抽象基类里，是一个普通的类方法。
# query、execute只是在基类中进行类声明，给出了描述，但并没有实现
# 它限定了继承Database的子类必须实现这两个方法

class Component1(Database):
    def __init__(self, host, user, password):
        self.register(host, user, password)

    @staticmethod
    def execute(sql_string):
        print(sql_string)

    def query(self, *args):
        sql_string = "SELECT ID FROM db_name"
        self.execute(sql_string)

    def test(self):
        print('Component1')


class Component2(Database):
    def __init__(self, host, user, password):
        self.register(host, user, password)

    @staticmethod
    def execute(sql_string):
        print(sql_string)

    def query(self, *args):
        sql_string = "SELECT NAME FROM db_name"
        self.execute(sql_string)

    def test(self):
        print('Component2')


comp1 = Component1("00.00.00.00", "abc", "000000")
comp2 = Component2("11.11.11.11", "ABC", "111111")
comp1.query()
comp2.query()

'''输出结果：
Host : 00.00.00.00
User : abc
Password : 000000
Register Success!
Host : 11.11.11.11
User : ABC
Password : 111111
Register Success!
SELECT ID FROM db_name
SELECT NAME FROM db_name'''
