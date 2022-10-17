from collections import deque


T = int(input())
dx = [-1,-2,-1,-2,2,1,1,2]
dy = [-2,-1,2,1,-1,-2,2,1]
def bfs(x, y, graph, n):
    q = deque([(x, y)])
    graph[x][y] = 1

    while q:
        a, b = q.popleft()
        for i in range(8):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[a][b] + 1
                q.append((nx, ny))
                if nx == d1 and ny == d2:
                    q = deque([])

for _ in range(T):
    n = int(input())
    graph = [[0] * n for _ in range(n)]
    x, y = map(int, input().split())
    d1, d2 = map(int, input().split())
    bfs(x, y, graph, n)
    print(graph[d1][d2] - 1)