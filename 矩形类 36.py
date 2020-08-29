class Rectangle:
    length = 0
    width = 0

    def get_length(self):
        self.length = int(input('输入矩形长： '))

    def get_width(self):
        self.width = int(input('输入矩形宽： '))

    def culcalate(self):
        s = self.width * self.length
        print(f'所设置的矩形面积是{s}')


p = Rectangle()
p.get_length()
p.get_width()
p.culcalate()
