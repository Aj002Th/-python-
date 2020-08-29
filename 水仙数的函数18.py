def find():
    for i in range(100,1000):
        a = 0
        temp = i
        while temp:
            a += (temp%10) ** 3
            temp = (temp//10)
        if a == i:
            print(a)
    
find()   
