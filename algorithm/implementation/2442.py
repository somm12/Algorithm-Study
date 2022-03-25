n = int(input())

for i in range(n):
    for k in range(n-1,i,-1):
        print(" ",end='')
    for k in range(0,i+1):
        print("*",end='')
    for k in range(0,i):
        print("*",end='')
    print() 