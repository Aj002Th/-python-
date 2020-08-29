temp = input('please input the password: ')
a = 3
while a > 1:
    i = str(a)
    if '*' in temp:
        print('the password can not have "*"!',end="")
        print('you have ' + i + 'chances!',end="")
        temp = input('please input the password: ')
    elif temp == 'curry':
        print('password is correct,enter the program...')
        break
    else:
        a -= 1
        i = str(a)
        print('the password you input is wrong!',end="")
        print('you have ' + i + 'chances!',end="")
        temp = input('please input the password: ')
if a == 1:
    print('chance is out ,over!')
else:
    print('')
