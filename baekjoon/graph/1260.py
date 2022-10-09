from collections import deque
import sys
input = sys.stdin.readline
n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for g in graph:
    g.sort()

def dfs(graph, visited, start):
    visited[start] = True
    print(start, end = ' ')
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, visited, i)

visited = [False] * (n + 1)
dfs(graph, visited, v)
print()

def bfs(graph, visited, start):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
visited = [False] * (n + 1)
bfs(graph, visited, v)