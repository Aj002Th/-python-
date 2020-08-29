def gcd(x,y,):
    if y != 0:
        a1 = x%y
        x = y
        y = a1
        return gcd(x,y)
    else:
        return x
print(gcd(1997,615))
