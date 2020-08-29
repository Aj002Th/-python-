class Mis:
    def __getattr__(self, item):
        print('该属性不存在！')


a = Mis()
print(a.no)