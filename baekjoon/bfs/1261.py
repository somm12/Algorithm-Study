from collections import deque
import sys
input = sys.stdin.readline
m, n = map(int, input().split())
visited = [[-1] * m for _ in range(n)]
room = []
dx = [ -1,1,0,0]
dy = [0,0,-1,1]
for _ in range(n):
    room.append(list(map(int,input().rstrip())))

def bfs(x,y):
    q = deque([(x,y)])
    visited[x][y] = 0
    while q:
        a, b = q.popleft()
        
        for i in range(4):
            nx = dx[i] + a
            ny = dy[i] + b
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if visited[nx][ny] == -1:
                if room[nx][ny] == 1:#벽일때
                    visited[nx][ny] = visited[a][b] + 1
                    q.append((nx, ny))
                else:#벽이 아닐때
                    visited[nx][ny] = visited[a][b]
                    q.appendleft((nx, ny))
           
bfs(0,0)
print(visited[n-1][m-1])