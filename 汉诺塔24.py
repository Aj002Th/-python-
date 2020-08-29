def hanoi(n,x,y,z):
    if n ==1:
        print(x,'->',z)
    else:
        hanoi(n-1,x,z,y)
        print(x,'->',z)
        hanoi(n-1,y,x,z)
n = int(input('input:'))
hanoi(n,x='X',y='Y',z='Z')
