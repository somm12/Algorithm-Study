dp = [[0] * 201 for _ in range(201)]
n, k = map(int,input().split())

for i in range(1, 201):
    dp[1][i] = i
for i in range(1, 201):
    dp[i][1] = 1
# for i in range(2, 201):
#     for j in range(1, 201):
#         res = 0
#         for m in range(1, j + 1):
#             res += (dp[i - 1][m] % 1000000000)
            
#         dp[i][j] = (res % 1000000000)

for i in range(2, 201):
    for j in range(2, 201):
        dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) % 1000000000

print(dp[n][k] % 1000000000)

# dp[n][k] = dp[n - 1][i]( i = 1 ~ k까지) => 이를 그대로 쓰면 3중 중첩문 + 여러번 같은 수를 반복해서 더하게됨.
# 하지만, dp[n - 1][i] 에서 i = 1 ~ k - 1 일때 => dp[n][k - 1] 와 같다.
# 따라서 dp[n][k] = dp[n][k - 1] + dp[n - 1][k]로 점화식을 간단히 할 수 있다.