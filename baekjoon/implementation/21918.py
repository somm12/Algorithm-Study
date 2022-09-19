import sys
input = sys.stdin.readline
n , m = map(int ,input().split())
arr = list(map(int ,input().split()))

for _ in range(m):
    a, b, c= map(int ,input().split())
    if a== 1:
        if c == 0:
            arr[b - 1] = 0
        else:
            arr[b - 1] = 1
    elif a == 2:
        for i in range(b-1 , c):
            if arr[i] == 1:
                arr[i] = 0
            else:
                arr[i] = 1
    elif a == 3:
        for i in range(b-1, c):
            arr[i] = 0
    else:
        for i in range(b-1 , c):
            arr[i] = 1

for j in range(n):
    print(arr[j], end=' ')
