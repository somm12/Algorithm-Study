def dfs(color, x, y, start_x, start_y, cnt):
    visited[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >=n or ny < 0 or ny >= m:
            continue
        if nx == start_x and ny == start_y and cnt >= 4:
            print('Yes')
            exit()
        if visited[nx][ny] == 0 and g[nx][ny] == color:
            
            dfs(color, nx, ny, start_x, start_y, cnt + 1)


n, m = map(int, input().split())
g = []
for _ in range(n):
    g.append(list(input()))
ans = 'No'
dx = [-1,1,0,0]
dy = [0,0, -1,1]

for i in range(n):
    for j in range(m):
        visited = [[0]* m for _ in range(n)]
        dfs(g[i][j], i, j, i, j, 1)
print(ans)