class Nstr(str):
    def __lshift__(self, other):
        list1 = list(self)
        for each in range(other):
            list1.append(list1.pop(0))
        self = ''.join(list1)
        return self

    def __rshift__(self, other):
        list1 = list(self)
        for each in range(other):
            list1.insert(0, list1.pop())
        self = ''.join(list1)
        return self


class Nstr1(str):
    def __lshift__(self, other):
        return self[other:] + self[:other]

    def __rshift__(self, other):
        return self[-other:] + self[:-other]


a = Nstr('I love FishC.com!')
print(a << 3)
print(a >> 3)

a = Nstr1('I love FishC.com!')
print(a << 3)
print(a >> 3)