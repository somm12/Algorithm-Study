from collections import deque


N,M = map(int, input().split())
arr = []
count = 1
#input with no space,, how?
for i in range(N):
    a = list(input())
    arr.append(a)

for i in range(N):
    for k in range(M):
        if arr[i][k] == 1:
            arr[i][k] = count
        count +=1

graph = [[]]
visited = [False]*(count-1)
for i in range(N):
    for k in range(M):
        if arr[i][k] != 0:
            a = []
            if arr[i-1][k] != 0 and i >0:
                a.append(arr[i-1][k])
            elif arr[i][k-1] != 0 and k >0:
                a.append(arr[i][k-1])
            elif arr[i][k+1] != 0 and k < M -1:
                a.append(arr[i][k+1])
            elif arr[i+1][k] != 0 and i < N-1:
                a.append(arr[i+1][k])
        graph.append(a)
depth = 0
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end='')
        depth = depth + 1
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

bfs(graph,1,visited)

print(count)

