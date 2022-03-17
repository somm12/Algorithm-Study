from collections import deque
import sys
sys.setrecursionlimit(10**6)

N,M = map(int,sys.stdin.readline().rstrip().split())
graph =[[] for i in range(N+1)]
for i in range(M):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)


                 
def bfs(graph,start, visited):
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            visited[i] = True
        for k in graph[i]:
            if not visited[k]:
                visited[k]= True

visited = [False] * (N+1)
visited[0] =True
count = 0
for i in range(1,N+1):
    if (visited[i] == False):
        bfs(graph,i,visited)
        count += 1
print(count)
