n = int(input())
arr = list(map(int, input().split()))
dp = [0] * n
dp[0] = arr[0]
for i in range(1, n):
        big = 0
        for j in range(i):
            if arr[j] < arr[i] and big < dp[j]:
                big = dp[j]
        dp[i] += big + arr[i]
print(max(dp))

#다른 방법
n = int(input())
dp = [0] * 1001
a = list(map(int, input().split()))
for i in a:
    dp[i] = max(dp[:i]) + i
print(max(dp))