def GCD(a, b):
    if a % b == 0:
        return b
    else:
        return GCD(b, a % b)

t = int(input())

for _ in range(t):
    arr = list(map(int,input().split()))
    n = arr[0]
    arr = arr[1:]

    ans = 0
    for i in range(n):
        for k in range(i + 1, n):
            ans += GCD(arr[i], arr[k])
    print(ans)