T = int(input())
max = 100000
a = 1000000009

dp = [[0] * 4 for _ in range(max + 1)]
dp[1] = [0,1,0,0]
dp[2] = [0,0,1,0]
dp[3] = [0,1,1,1]



for i in range(4, max + 1):
    dp[i][1] = dp[i - 1][2] + dp[i - 1][3]
    dp[i][2] = dp[i - 2][1] + dp[i - 2][3]
    dp[i][3] = dp[i - 3][1] + dp[i - 3][2]

    dp[i][1] %= a
    dp[i][2] %= a
    dp[i][3] %= a


for _ in range(T):
    n = int(input())
    print(sum(dp[n]) % a)
