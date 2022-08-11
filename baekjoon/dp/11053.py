n = int(input())

arr = list(map(int,input().split()))
dp = [0] * n
length = -1
dp[0] = 1

for i in range(1, n):
    for k in range(i):
        if arr[i] > arr[k]:
            if dp[k] > dp[i]:
                dp[i] = dp[k]
    dp[i] += 1
print(max(dp))
