n = int(input())
limit = 100001
dp = [[0] * 3 for _ in range(limit) ]

dp[1][0] = 1
dp[1][1] = 1
dp[1][2] = 1

for i in range(2, limit):
    dp[i][0] = (dp[i - 1][0] + dp[i-1][1] + dp[i-1][2]) % 9901
    dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % 9901
    dp[i][2] = (dp[i-1][0] + dp[i-1][1]) % 9901
print(sum(dp[n]) % 9901)
