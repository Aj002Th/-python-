class Fish:
    dead = 0

    def __init__(self):
        import random
        self.x = random.randint(0, 11)
        self.y = random.randint(0, 11)

    def move(self):
        if self.dead == 1:
            self.x = -5
            self.y = -5
        else:
            import random
            go = random.randint(1, 5)
            if go == 1:
                self.x += 1
                if self.x == 11:
                    self.x = 9
            elif go == 2:
                self.x -= 1
                if self.x == -1:
                    self.x = 1
            elif go == 3:
                self.y += 1
                if self.y == 11:
                    self.y = 9
            else:
                self.y -= 1
                if self.y == -1:
                    self.y = 1

    def die(self):
        global fish
        if self.x == t1.x and self.y == t1.y:
            self.dead = 1
            fish.pop()


class Turtle:
    action = 100
    dead = 0

    def __init__(self):
        import random
        self.x = random.randint(0, 11)
        self.y = random.randint(0, 11)

    def move(self):
        if self.dead == 1:
            self.x = -5
            self.y = -5
        else:
            import random
            go = random.randint(1, 5)
            how_much = random.randint(1, 3) # 移动次数
            self.action -= how_much
            for each in range(0, how_much):
                if go == 1:
                    self.x += 1
                    if self.x == 11:
                        self.x = 9
                elif go == 2:
                    self.x -= 1
                    if self.x == -1:
                        self.x = 1
                elif go == 3:
                    self.y += 1
                    if self.y == 11:
                        self.y = 9
                else:
                    self.y -= 1
                    if self.y == -1:
                        self.y = 1

    def die(self):
        if self.action == 0:
            self.dead = 1

    def eat(self):
        if self.x == new_fish.x and self.y == new_fish.y:
            self.action += 20


t1 = Turtle()
fish = []
for i in range(10):
    new_fish = Fish()
    fish.append(new_fish)

while 1:
    if t1.action == 0:
        print('乌龟累死了！')
        break
    if fish:
        print('鱼被吃完了！')
        break
    t1.move()
    new_fish.die()
    new_fish.move()
    t1.die()
