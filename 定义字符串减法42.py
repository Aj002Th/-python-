class Nstr(str):
    def __sub__(self, other):
        for each in other:
            if each in self:
                self = self.strip(each)  # 有问题！！strip只能删除头尾部分
        return self


class Nstr1(str):
    def __sub__(self, other):
        return self.replace(other, '')


a = Nstr('I love FishC.com!iiiiiiii')
b = Nstr('i')
print(a - b)

a = Nstr1('I love FishC.com!iiiiiiii')
b = Nstr1('i')
print(a - b)