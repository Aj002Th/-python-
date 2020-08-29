a = 99
reslt = 0
print('here are the answer:')
while a <= 999:
    a += 1
    b = str(a)
    for c in b:
        i = int(c)
        reslt = reslt + i ** 3
    if reslt == a:
        print(a)
    else:
        continue
