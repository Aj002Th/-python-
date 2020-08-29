class Demo:
    x = "FishC!"

    def __getattribute__(self, item):
        print(super().__getattribute__(item))
        # 注意这里的参数数量！！还有含义是指访问的属性名


demo = Demo()
demo.x
demo.x = "X-man"
demo.x


class Demo:
    def __getattr__(self, name):
        self.name = 'FishC'
        return self.name  # 返回值不加以表示是不会表现出来的


demo = Demo()
demo.x
demo.x = "X-man"
demo.x
