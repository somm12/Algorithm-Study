from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
graph = [[] for _ in range(n + 1)]
count = 0
for _ in range(m):
    a, b = map(int ,input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False] * (n + 1)

def bfs(graph, start):
    q = deque([start])
    visited[start] = True
    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

for i in range(1, n + 1):
    if not visited[i]:
        bfs(graph, i)
        count += 1
print(count)