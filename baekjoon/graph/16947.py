from collections import deque
import sys

input = sys.stdin.readline
sys.setrecursionlimit(100000)

def dfs(v, start, cnt):
    global cycle
    if v == start and cnt >= 2:
        cycle = True
        return
    
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i, start, cnt + 1)
        elif i == start and cnt >= 2:
            dfs(i, start, cnt)
def area():
    q = deque()
    for i in range(n):
        if station[i]:
            ans[i] = 0
            q.append(i)
    while q:
        v = q.popleft()
        for i in graph[v]:
            if ans[i] == -1:
                ans[i] = ans[v] + 1
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
    dfs(i, i, 0)
    if cycle:
        station[i] = True

area()