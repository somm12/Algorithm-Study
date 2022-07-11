import sys
input = sys.stdin.readline
n = int(input())
arr = []

for _ in range(n):
    c = list(input().split())

    if len(c) == 2:
        arr.append(int(c[1]))
    else:
        if c[0] == "pop":
            if len(arr) == 0:
                print(-1)
            else:
                print(arr.pop())
        elif c[0] == "size":
            print(len(arr))
        
        elif c[0] == "empty":
            if len(arr) == 0:
                print(1)
            else:
                print(0)
        elif c[0] == "top":
            if len(arr) == 0:
                print(-1)
            else:
                print(arr[-1])