from collections import deque


n, m = map(int,input().split())
graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for _ in range(n):
    graph.append(list(map(int, input().split())))
def bfs(x, y):
    q = deque([(x,y)])
    while q:
        a, b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[a][b] + 1
                q.append((nx,ny))
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            bfs(i,j)
            for v in graph:
                for i in v:
                    if i != 0 and i != 1:
                        print(i - 2, end=' ')
                    elif i == 1:
                        print(-1, end=' ')
                    else:
                        print(i, end=' ')
                print()
            exit()