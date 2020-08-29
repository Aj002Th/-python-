class Person:
    name = '小甲鱼'

    def print_name(self):
        print(self.name)

    def set_name(self):
        self.name = input('请输入名字')


p = Person()
p.set_name()
p.print_name()
