n = int(input())

for i in range(n):
    for k in range(0,i):
        print(" ",end='')
    for k in range(i,n):
        print("*",end='')
    print()