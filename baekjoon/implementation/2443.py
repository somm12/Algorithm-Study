n = int(input())

for i in range(n):
    for k in range(i):
        print(" ",end='')
    for k in range(i,n):
        print("*",end='')
    for k in range(i,n-1):
        print("*",end='')
    print()