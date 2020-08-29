def check(x):
    b = list(reversed(x))
    a = ""
    for each in b:
        a += str(each)
    if str(x) == a:
        return 1
    else:
        return 0
i = input('input: ')
if check(i):
    print('yes!')
else:
    print('no!')
