T = int(input())

for _ in range(T):
    n = int(input())
    dp = [[0] * n]
    for _ in range(2):
        dp.append(list(map(int,input().split())))
    for i in range(1, n):
        dp[0][i] = dp[0][i] + max(dp[0][i - 1], dp[1][i - 1], dp[2][i - 1])
        dp[1][i] = dp[1][i] + max(dp[0][i - 1], dp[2][i - 1])
        dp[2][i] = dp[2][i] + max(dp[0][i - 1], dp[1][i - 1])
    
    ans = max(dp[0][n - 1], dp[1][n - 1], dp[2][n - 1])
    print(ans)



