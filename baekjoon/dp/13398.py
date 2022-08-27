n = int(input())
arr = list(map(int,input().split()))

dp = [[0] * n for _ in range(2)]
# 최소한 한 개는 선택해야함.
dp[0][0] = arr[0]
ans = -1001

if n > 1:
    for i in range(1, n):
        # 0 -> 원소를 제거하지 않는 경우. 제거가 없는 연속 합 중 최대합.
        # 1 -> i까지 원소들 중 하나 제거하는 경우 중 최대합
        dp[0][i] = max(arr[i], dp[0][i - 1] + arr[i])
        # i - 1번째 까지 원소들 중 하나 제거한 경우들, i 번째 원소를 제거 한 경우 최대 연속합.
        dp[1][i] = max(arr[i] + dp[1][i - 1], dp[0][i - 1])
        ans = max(ans, dp[0][i], dp[1][i])
    print(ans)
else:
    print(dp[0][0])