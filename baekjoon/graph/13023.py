import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
visited = [False] * n

def dfs(L ,next):
    if L == 4:
        print(1)
        exit()
    for i in arr[next]:
        if not visited[i]:
            visited[i] = True
            dfs(L + 1, i)
            visited[i] = False

for i in range(n):
    visited[i] = True
    dfs(1, i)
    visited[i] = False
print(0)