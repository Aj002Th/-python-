class Nstr(float):
    def __new__(cls, arg=0):
        if isinstance(arg, str):
            total = 0
            for each in arg:
                total += ord(each)
            arg = total
        return float.__new__(cls, arg)


a = Nstr('FishC')
b = Nstr('love')
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
