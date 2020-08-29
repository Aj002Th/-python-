class Int(int):

    def __new__(cls, s):
        if isinstance(s, str):
            i = 0
            for each in s:
                i += ord(each)
            return int.__new__(cls, i)
        else:
            return int.__new__(cls, s)


print(Int('abc'))
print(Int(456))
