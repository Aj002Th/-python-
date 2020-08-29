while 1:
    a = input('input a int ,(knck "q" to quit): ')
    if a == 'q':
        break
    else:
        i = int(a)
        a16 = '%x' % i
        a8 = '%o' % i
        a2 = bin(i)
        print('10 to 16:  ', 'i' , '=>' , a16)
        print('10 to 8: ', 'i' , '=>' , a8)
        print('10 to 2:', 'i' , '=>' , a2)
