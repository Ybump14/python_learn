'''8.8 子类中扩展property
问题:
在子类中，你想要扩展定义在父类中的property的功能。

解决方案:
考虑如下的代码，它定义了一个property'''


class aa:
    @property
    def name(self):
        print('iam aa print')
        return self._name

    # Setter function
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._name = value
        print('iam test')


class test(aa):
    @property
    def name(self):
        print('iam test print')
        return self._name

    # Setter function
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._name = value
        print('iam test')


class Person(test):
    def __init__(self, name):
        self.name = name

    # Getter function
    @property
    def name(self):
        print('iam person print')
        return self._name

    # Setter function
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._name = value
        print('iam person')

    # Deleter function
    @name.deleter
    def name(self):
        raise AttributeError("Can't delete attribute")


class SubPerson(Person):
    @property
    def name(self):
        print('Getting name')
        return super(test, Person).name.__get__(self)

    @name.setter
    def name(self, value):
        print('Setting name to', value)
        super(Person, Person).name.__set__(self, value)

    @name.deleter
    def name(self):
        print('Deleting name')
        super(SubPerson, SubPerson).name.__delete__(self)


# a = Person('yangjiajun')
# print(a.name, '\n')  # yangjiajun

b = SubPerson('jojo')
print(b.name)
# Setting name to jojo
# iam test
# Getting name
# iam aa print
# jojo
