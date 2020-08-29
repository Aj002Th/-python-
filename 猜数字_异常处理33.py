import random
answer = random.randint(1,9)
times = 2
guss = 0
print("----my game----")
temp = input("guss the number i think is:")
while guss != answer and times > 0:
    try:
        guss = int(temp)
    except ValueError:
        print('请输入一个数字！')
        times = 0
        break
    if guss == answer:
            print("nice,you got it!")
            print("but no present you will get")
    else:
        if guss > answer:
                    print("your number is too big!")
        else:
                    print("your number is too small!")
        temp = input("try again!!you will make it.the number i think is:")
        times = times-1

if times>0:
        print("you win.game over")
else:
        print("time is out.you lose.game over.")
