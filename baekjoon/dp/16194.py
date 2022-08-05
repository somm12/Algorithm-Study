n = int(input())
p = list(map(int,input().split()))
p.insert(0,0)
dp = [10000000 for _ in range(n + 1)]
dp[0] = 0
dp[1] = p[1]

for i in range(1, n + 1):
    for k in range(1, i + 1):
        dp[i] = min(dp[i], dp[i - k] + p[k])
print(dp[n])
