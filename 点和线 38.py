import math


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def getx(self):
        print(self.x)

    def gety(self):
        print(self.y)


class Line:
    def __init__(self, pp1, pp2):
        self.p1 = pp1
        self.p2 = pp2

    def get_line(self):
        long = math.sqrt((self.p1.x - self.p2.x) ** 2 + (self.p1.y - self.p2.y) ** 2)
        return (f'线段长度为{long}')


p1 = Point(2, 2)
p2 = Point(-2, 2)
line = Line(p1, p2)
length = line.get_line()
print(length)
