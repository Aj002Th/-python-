import random
answer = random.randint(1,9)
times = 2
guss = 0
print("----my game----")
temp = input("guss the number i think is:")
while guss != answer and times > 0:
    if temp.isdigit():
        guss = int(temp)
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
    else:
        print("why not use number?!please input a number!")
        temp = input("input the number i think is:")
if times>0:                
        print("you win.game over")
else:
        print("time is out.you lose.game over.")        
