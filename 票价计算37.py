class Ticket:
    price = 100
    workday = 1
    weekend = 1.2

    def __init__(self):
        import easygui as g
        self.man = g.multenterbox('人数统计', '游乐场票价计算', ['成人数量：', '儿童数量：'])
        self.day = g.boolbox('时间确定', '游乐场票价计算', ['工作日', '周末'])

    def how_much(self):
        money = int(self.man[0]) * self.price + int(self.man[1]) * self.price * 0.5
        if self.day:
            print(f'票价为{money}')
        else:
            print(f'票价为{money * 1.2}')


play = Ticket()
play.how_much()
