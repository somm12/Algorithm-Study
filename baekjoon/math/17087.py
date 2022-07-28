def GCD(a, b):
    if a % b == 0:
        return b
    else:
        return GCD(b, a % b)

N, S = map(int,input().split())
arr = list(map(int,input().split()))

if N == 1:
    print(abs(arr[0] - S))
else:
    for i in range(len(arr)):
        arr[i] = abs(arr[i] - S)
    ans = arr[0]
    for i in range(1, len(arr)):
        ans = GCD(ans, arr[i])
    print(ans)
