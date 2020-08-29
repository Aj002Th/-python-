def nb(x,y):
    while 1:
        i = y
        y = x % y
        if y == 0:
            return i
print(nb(1997,65))        
    
