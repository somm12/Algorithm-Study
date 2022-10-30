from collections import deque
import sys
# 재귀의 깊이를 지정.
input = sys.stdin.readline
# sys.setrecursionlimit(100000)

def dfs(start, now, cnt):
    global cycle
    if now == start and cnt >= 3:
        cycle = True
        return
    
    visited[now] = True
    for i in graph[now]:
        if not visited[i]:
            dfs(start, i, cnt + 1)
        elif i == start and cnt >= 3:
            dfs(start, i, cnt)
def area():
    q = deque()
    for i in range(n):
        if station[i]:
            ans[i] = 0
            q.append(i)
    while q:
        x = q.popleft()
        for i in graph[x]:
            if ans[i] == -1:
                ans[i] = ans[x] + 1
                q.append(i)
    for i in ans:
        print(i, end=' ')

n = int(input())
graph = [[] for _ in range(n)]
station = [False] * n
ans = [-1] * n

for _ in range(n):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

for i in range(n):
    visited = [False] * n
    cycle = False
    dfs(i, i, 1)
    if cycle:
        station[i] = True

area()