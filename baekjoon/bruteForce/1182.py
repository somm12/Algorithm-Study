import sys
input = sys.stdin.readline
n,s = map(int, input().split())
arr = list(map(int, input().split()))
count = 0

def dfs(L, total):
    global count
    if L >= n:
        return
    total += arr[L]
    if total == s:
        count += 1
    dfs(L + 1, total)
    dfs(L + 1, total - arr[L])

dfs(0,0)
print(count)