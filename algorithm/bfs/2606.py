from collections import deque
n = int(input())
pair_size = int(input())
visited = [False] * n
graph = [[] for i in range(n+1)]

for i in range(pair_size):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start,graph,visited):
    defected = 0
    queue = deque([start])
    visited[start] = True
    while queue:
        value = queue.popleft()
        for i in graph[value]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                defected += 1
    return defected
print(bfs(1,graph,visited))
