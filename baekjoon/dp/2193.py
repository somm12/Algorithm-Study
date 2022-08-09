dp = [[0] * 2 for _ in range(91)]
n = int(input())

dp[1] = [0,1]
for i in range(2, 91):
    dp[i][0] = dp[i - 1][0] * 1 + dp[i - 1][1] * 1
    dp[i][1] = dp[i - 1][0] * 1
print(sum(dp[n]))