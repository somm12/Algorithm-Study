s = [1, 1, 2, 2, 2, 8]
arr = list(map(int, input().split()))
for i in range(6):
    print(s[i] - arr[i], end=' ')
