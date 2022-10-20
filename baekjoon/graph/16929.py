import sys
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
graph = []
for _ in range(n):
    graph.append(list(input()))

visited = [[0] * m for _ in range(n)]
ans = False
dx = [-1,1,0,0,]
dy = [0,0, -1,1]
def sol(color, x, y, cnt, start_x, start_y):
    global ans
    if ans:
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >=n or ny < 0 or ny >= m:
            continue
        if graph[nx][ny] == color and cnt >= 4 and start_x == nx and start_y == ny:
            ans = True
            return
        if graph[nx][ny] == color and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            sol(color, nx, ny, cnt + 1, start_x, start_y)
            visited[nx][ny] = 0


for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        sol(graph[i][j], i, j, 1, i, j)
        if ans == True:
            print('Yes')
            exit()
print('No')