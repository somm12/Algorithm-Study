n = int(input())
dp = []

for _ in range(n):
    dp.append(list(map(int,input().split())))

for i in range(1, n):
    for j in range(len(dp[i])):
        if j == 0:
            dp[i][j] += dp[i - 1][j]
        elif j == len(dp[i]) - 1:
            dp[i][j] += dp[i - 1][j - 1]
        else:
            a = dp[i][j] + dp[i - 1][j - 1]
            b = dp[i][j] + dp[i - 1][j]
            dp[i][j] = max(a, b)
print(max(dp[n - 1]))        