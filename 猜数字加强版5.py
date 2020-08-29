import random
answer = random.randint(1,9)
times = 2
print("----my game----")
temp = input("guss the number i think is:")
if temp.isdigit():
        guss = int(temp)
        if guss == answer:
                print("nice,you win")
                print("but no present you will get")
        else:
            if guss > answer:
                        print("your number is too big!")
            else:
                        print("your number is too small!")
            while guss !=answer and times > 0:
                temp = input("try again!!you will make it.the number i think is:")
                guss = int(temp)
                times = times-1
                if guss == answer:
                    print("nice,you win")
                    print("but no present you will get")
                else:
                    if guss > answer:
                        print("your number is too big!")
                    else:
                        print("your number is too small!")
else:
     print("why not use number?!")   
if times>0:                
        print("game over")
else:
        print("time is out.game over.")
        
