n = int(input())

square = [i * i for i in range(1, 320)]
dp = [0] * (n + 1)
res = []

for i in range(1, n + 1):
    for j in square:
        if j > i:
            break
        res.append(dp[i - j])
    dp[i] = min(res) + 1
    res = []
print(dp[n])