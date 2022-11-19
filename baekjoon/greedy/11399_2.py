import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
ans = 0
now = 0
for v in arr:
    now += v
    ans += now
print(ans)
