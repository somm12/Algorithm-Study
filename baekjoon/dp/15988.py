limit = 1000001
dp = [0] * limit

dp[1] = 1
dp[2] = 2
dp[3] = 4

a = 1000000009

for i in range(4 , limit):
    dp[i] = (dp[i - 1] % a) + (dp[i - 2] % a) + (dp[i - 3] % a)
    dp[i] %= a

n = int(input())

for i in range(n):
    m = int(input())
    print(dp[m])