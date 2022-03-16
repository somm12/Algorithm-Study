from collections import deque

N,M = map(int,input().split())
graph =[[] for i in range(N+1)]
for i in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
                   
def bfs(graph,start, visited):
    queue = deque([start])
    if visited[start] == True:
        return 0
    else:
        visited[start] = True
        while queue:
            v = queue.popleft()
            if v >= N:
                visited[v] = True
                continue
            else:
                for i in graph[v]:
                    if not visited[i]:
                        queue.append(i)
                        visited[i] = True
        return 1

visited = [False] * (N+1)

result = 0
for i in range(1,N+1):
    result = result + bfs(graph,i,visited)    
print(result)

