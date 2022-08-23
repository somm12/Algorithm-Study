n = int(input())
arr = list(map(int,input().split()))
dp = [0]*1001
for val in arr:
    if val == 1000:
        dp[val] = 1
    else:
        dp[val] = max(dp[val + 1:]) + 1
print(max(dp))
