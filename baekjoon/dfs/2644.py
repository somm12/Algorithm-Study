from collections import deque


n = int(input())
target1, target2 = map(int,input().split())
num_of_relation = int(input())

graph = [[] for i in range(n+1)]
depth = [0 for i in range(n+1)]
#default value for the result value
depth[0] = -1

visited = [False] * (n+1)
result = 0

for i in range(num_of_relation):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)



def bfs(graph,visited,start,depth):
    visited[start] = True
    queue = deque([start])
    while queue:
        value = queue.popleft()
        for i in graph[value]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                depth[i] = depth[value] + 1
                if i == target2:
                    depth[0] = depth[target2]
                
        
    

bfs(graph,visited,target1,depth)
print(depth[0])


