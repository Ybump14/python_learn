'''访问限制
练习
请把下面的Student对象的gender字段对外隐藏起来，用get_gender()和set_gender()代替，并检查参数有效性：'''


class Student(object):
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if isinstance(name, str):
            self.__name = name
        else:
            raise TypeError('name must be string')

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        if isinstance(gender, str):
            self.__gender = gender
            return self.__gender
        else:
            raise TypeError('gender must be string')


bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')


class Student(object):
    def __init__(self, name, gender):
        self._name = name
        self._gender = gender

    def get_gender(self):
        return self._gender

    def set_gender(self, gender):
        if isinstance(gender, str):
            self._gender = gender
            return self._gender
        else:
            raise TypeError('gender must be string')
