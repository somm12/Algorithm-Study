import sys
input = sys.stdin.readline

def dfs(color, x, y, cnt, start_x, start_y):
    global ans
    if ans:
        return
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx <0 or nx >= n or ny < 0 or ny >= m:
            continue
        if cnt >= 4 and nx == start_x and ny ==start_y:
            ans = True
            return
        if graph[nx][ny] == color and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            dfs(color, nx, ny, cnt + 1, start_x, start_y)
            visited[nx][ny] = 0


n, m = map(int, input().split())
graph = [[i for i in input().rstrip()] for _ in range(n)]

visited = [[0] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = False

for i in range(n):
    for j in range(m):
        start_x, start_y = i, j
        visited[start_x][start_y] = 1
        dfs(graph[i][j], i, j, 1, start_x,start_y)
        if ans:
            print('Yes')
            exit()
print('No') 
