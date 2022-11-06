from collections import deque

m, n = map(int,input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int,input())))
dx = [-1,1,0,0]
dy = [0,0,-1,1]
dist = [[-1] * m for _ in range(n)]

def bfs():
    q = deque([(0,0)])
    dist[0][0] = 0
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if dist[nx][ny] == -1:
                if graph[nx][ny] == 1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx,ny))
                else:
                    dist[nx][ny] = dist[x][y]
                    q.appendleft((nx,ny))
bfs()
print(dist[n-1][m-1])