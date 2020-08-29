def in2(x):
    nb = ''
    list = []
    while x:
        i = x%2
        x = x//2
        list.append(i)
    while list:
        nb += str(list.pop())
    return nb
print(in2(10))
        
