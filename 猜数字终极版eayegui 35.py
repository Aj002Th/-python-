import random
from easygui import *

answer = random.randint(1, 9)
times = 2
guss = 0
print("----my game----")
temp = enterbox("guss the number i think is:", '猜数字游戏')
while guss != answer and times > 0:
    if temp.isdigit():
        guss = int(temp)
        if guss == answer:
            msgbox("nice,you got it!")
            msgbox("but no present you will get")
        else:
            if guss > answer:
                msgbox("your number is too big!")
            else:
                msgbox("your number is too small!")
            temp = enterbox("try again!!you will make it.the number i think is:", '猜数字游戏')
            times = times - 1
    else:
        msgbox("why not use number?!please input a number!")
        temp = enterbox("input the number i think is:", '猜数字游戏')
if times > 0:
    msgbox("you win.game over", '猜数字游戏')
else:
    msgbox("time is out.you lose.game over.", '猜数字游戏')
