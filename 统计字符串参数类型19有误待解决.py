def calculate(*x):
    list1 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x',
             'c', 'v', 'b', 'n', 'm']
    list2 = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    list3 = [' ']
    a, b, c, d = 0, 0, 0, 0
    long = len(x)
    for i in range(long):
        y = list(x[i])
        for each in y:
            if each in list1:
                a += 1
            if each in list2:
                b += 1
            if each in list3:
                c += 1
            if each not in list1 and each not in list2 and each not in list3:
                d += 1
        print(i + 1, a, b, c, d)


i = 'I love fishc.com.', 'I love you, you love me.'
calculate(i)
