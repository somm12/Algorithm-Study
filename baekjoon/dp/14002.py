n = int(input())
arr = list(map(int,input().split()))

dp = [0] * n
ans = []

for i in range(n):
    for k in range(i):
        if arr[k] < arr[i] and dp[k] > dp[i]:
            dp[i] = dp[k]
    dp[i] += 1

max_length = max(dp)
max_index = dp.index(max_length)
ans.append(arr[max_index])

for i in range(max_index - 1, -1, -1):
    if arr[max_index] > arr[i] and dp[i] == dp[max_index] - 1:
        ans.append(arr[i])
        max_index = i
ans = ans[::-1]

print(max_length)
for val in ans:
    print(val, end=' ')