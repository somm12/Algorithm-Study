n = int(input())

for i in range(0,n):
    for k in range(n-1,i,-1):
        print(" ",end='')
    for k in range(0,i+1):
        print("*",end='')
    print()

for i in range(0,n-1):
    for k in range(0,i+1):
        print(" ",end='')
    for k in range(n-1,i,-1):
        print("*",end='')
    print()  