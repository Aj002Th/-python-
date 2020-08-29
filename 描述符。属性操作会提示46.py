class MyDes:  # 是个描述符
    def __init__(self, value, name):
        self.name = name
        self.value = value

    def __get__(self, instance, owner):
        print(f'正在获取属性{self.name}')
        return self.value

    def __set__(self, instance, value):
        print(f'正在修改属性{self.name}')
        self.value = value

    def __delete__(self, instance):
        print(f'正在删除属性{self.name}')
        print('这个变量没法删除')


class Test:
    x = MyDes(10, 'x')


test = Test()
y = test.x
print(y)
test.x = 8
del test.x
print(test.x)
