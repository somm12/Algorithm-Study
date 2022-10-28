import sys
from tracemalloc import start
n, m = map(int, sys.stdin.readline().split())

ans = 'No'
board = []
for _ in range(n):
    board.append(list(sys.stdin.readline().rstrip()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def sol(color, cnt, start_x, start_y, x, y):
    global ans
    if ans == 'Yes':
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx == start_x and ny == start_y and cnt >= 4:
            ans = 'Yes'
            break
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if visited[nx][ny] == 0 and color == board[nx][ny]:
            visited[nx][ny] = 1
            sol(color, cnt + 1, start_x, start_y, nx, ny)
    
for i in range(n):
    for j in range(m):
        visited = [[0] * m for _ in range(n)]
        visited[i][j] = 1
        sol(board[i][j], 1, i, j, i, j)
        if ans == 'Yes':
            print(ans)
            exit()
print(ans)