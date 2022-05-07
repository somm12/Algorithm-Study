from collections import deque
n, m = map(int , input().split())
graph = []
for i in n:
  graph.append(list(map(int, input().split())))

#상하 좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
  queue = deque()
  queue.append((x,y))
  while queue:
    x,y = queue.popleft()
    for i in 4:
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 1 or ny < 1 or nx > n or ny > m:
        continue
      if graph[nx][ny] == 0:
        continue
      if graph[nx][ny] == 1:
        queue.append((nx,ny))
        graph[nx][ny] = graph[nx][ny] + 1

bfs(0,0)
result = bfs(graph[n-1][m-1])
print(result)