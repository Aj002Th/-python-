def power(x,y):
    if y ==1:
        return x
    else:
        x *= x
        y -= 1
        return power(x,y)
i = power(2,3)
print(i)

def power(x, y):
    if y:
        return x * power(x, y-1)
    else:
        return 1
    
print(power(2, 3))
