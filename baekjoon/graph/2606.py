from collections import deque
from glob import glob


n = int(input())
m = int(input())
count = 0
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    global count
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        count += 1
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
bfs(1)
print(count - 1)