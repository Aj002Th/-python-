def likebin(x):
    y = x%2
    x //= 2
    if x != 0:
        return str(y)+likebin(x)
    else:
        return '1'
i = list(reversed(likebin(25)))
for each in i :
    print(each,end="")
        
    
