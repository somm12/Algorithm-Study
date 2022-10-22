from collections import deque

def bfs():
    q = deque([])
    for i in range(n):
        for j in range(m):
            if g[i][j]  == 1:
                q.append((i,j))
    while q:
        a, b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if g[nx][ny] == 0:
                g[nx][ny] = g[a][b] + 1
                q.append((nx,ny))

m, n = map(int, input().split())
g = []
for _ in range(n):
    g.append(list(map(int,input().split())))
ans = -1e9
dx = [-1,1,0,0]
dy = [0,0,-1,1]

bfs()

for i in range(n):
    for j in range(m):
        if g[i][j] == 0:
            print(-1)
            exit()
        ans = max(ans, g[i][j])
print(ans - 1)