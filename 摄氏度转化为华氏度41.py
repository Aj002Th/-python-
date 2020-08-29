class C2F(float):
    def __new__(cls, f):
        c = f * 1.8 + 32
        return float.__new__(cls, c)


print(C2F(32))
