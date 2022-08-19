limit = 1001
dp = [[0] * 10 for _ in range(limit)]

for i in range(10):
    dp[1][i] = 1

for i in range(2, limit):
    for j in range(10):
        if j == 0:
            dp[i][j] = sum(dp[i - 1]) % 10007
        else:
            dp[i][j] = (dp[i][j - 1] - dp[i - 1][j - 1]) % 10007
n = int(input())
print(sum(dp[n]) % 10007)