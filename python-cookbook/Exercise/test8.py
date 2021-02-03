def do():
    a = int(input("Please input the first side:"))  # 输入第一条边
    b = int(input("Please input the second side:"))  # 输入第二条边
    c = int(input("Please input the third side:"))  # 输入第三条边
    if (a + b > c) and (a + c > b) and (b + c > a):  # 判断是否是三角形
        if a == b == c:
            print("This is a equilateral triangle")  # 等边三角形
        elif (a == b or a == c or b == c):
            print("This is a isosceles triangle")  # 等腰三角形
        elif (a * a + b * b == c * c) or (a * a + c * c == b * b) or (c * c + b * b == a * a):
            print("This is a right triangle")  # 直角三角形
        else:
            print("This is a scalene triangle")  # 不规则三角形
    else:
        print("This isn't a triangle")  # 不是三角形


class test:

    def __init__(self, data):
        data.sort()
        self.data = data
        for i in data:
            if not isinstance(i, int):
                raise TypeError('你输入的边中，存在非整数边')

    def gg(self, a, b, c):
        if a + b > c:
            return True
        return False

    def hh(self, a, b):
        if a == b:
            return True
        return False

    def zz(self, a, b, c):
        if a * a + b * b == c * c:
            return True
        return False

    def ab(self):
        a = None
        if not self.gg(self.data[0], self.data[1], self.data[2]):
            print('不是三角形')
            return
        if not self.gg(self.data[0], self.data[2], self.data[1]):
            print('不是三角形')
            return
        if not self.gg(self.data[1], self.data[2], self.data[0]):
            print('不是三角形')
            return
        if self.hh(self.data[0], self.data[1]) or self.hh(self.data[1], self.data[2]) or self.hh(self.data[0],
                                                                                                 self.data[2]):
            a = '这是一个等腰三角形'
        if self.hh(self.data[0], self.data[1]) and self.hh(self.data[1], self.data[2]):
            a = '这是一个等边三角形'
        if self.zz(self.data[0], self.data[1], self.data[2]):
            a = '这是一个直角三角形'
        if a:
            print(a)
        else:
            print('这是一个不规则三角形')


test([5, 4, 3]).ab()
