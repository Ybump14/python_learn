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


class Test_triangle:

    def __init__(self, data):
        self.data = sorted(data)
        for i in data:
            if not isinstance(i, int):
                raise TypeError('你输入的第%s条边不是整数' % (data.index(i) + 1))
            elif i <= 0:
                raise TypeError('你输入的第%s条边不是正整数' % (data.index(i) + 1))

    def triangle(self, a, b, c):
        if a + b > c:
            return True
        return False

    def isosceles_triangle(self, a, b):
        if a == b:
            return True
        return False

    def right_triangle(self, a, b, c):
        if a * a + b * b == c * c:
            return True
        return False

    def is_triangle(self):
        a = None
        if not self.triangle(self.data[0], self.data[1], self.data[2]):
            print('不是三角形')
            return
        if self.isosceles_triangle(self.data[0], self.data[1]) or \
                self.isosceles_triangle(self.data[1], self.data[2]) or \
                self.isosceles_triangle(self.data[0], self.data[2]):
            a = '这是一个等腰三角形'
        if self.isosceles_triangle(self.data[0], self.data[1]) and \
                self.isosceles_triangle(self.data[1], self.data[2]):
            a = '这是一个等边三角形'
        if self.right_triangle(self.data[0], self.data[1], self.data[2]):
            a = '这是一个直角三角形'
        if a:
            print(a)
        else:
            print('这是一个不规则三角形')


Test_triangle([1, 2, 1]).is_triangle()
