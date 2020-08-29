class C:
    def __init__(self, *a):
        if a == ():
            print('没有参数传入')
        else:
            print(f"传入了 {len(a)} 个参数，分别是：{a}")


c = C()
a = C(1, 2, 3)
