N,X = map(int, input().split())
arr = [0 for i in range(N)]
a = list(map(int,input().split()))
for i in range(N):
    arr[i] = a[i]


for i in range(N):
    if arr[i] < X:
        print(arr[i], end=' ')