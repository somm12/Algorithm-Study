from collections import deque

N,M,V = map(int,input().split())
visited_dfs = [False] * (N+1)
visited_bfs = [False] * (N+1)
graph = [[] for i in range(N+1)]
for i in range(M):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(graph,visited,start):
    visited[start] = True
    print(start, end=' ')
    for i in graph[start]:
        if not visited[i]:
            dfs(graph,visited,i)

def bfs(graph,visited,start):
    visited[start] = True
    print(start,end='')
    queue = deque([start])
    while queue:
        value = queue.popleft()
        for i in graph[value]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                print(i,end=' ')
                



dfs(graph,visited_dfs,V)
print()
bfs(graph,visited_bfs,V)
