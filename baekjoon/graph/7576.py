from collections import deque


graph = []
m,n = map(int, input().split())
for _ in range(n):
    graph.append(list(map(int, input().split())))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q = deque([])

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
           q.append((i, j))
      
while q:
    a, b = q.popleft()
    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if graph[nx][ny] == 0:
            graph[nx][ny] = graph[a][b] + 1
            q.append((nx, ny))

ans = -1e9
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print(-1)
            exit()
        ans = max(ans, graph[i][j])
if ans == 1:
    print(0)
else:
    print(ans - 1)
