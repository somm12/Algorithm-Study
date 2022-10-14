from collections import deque

n,m = map(int,input().split())
graph = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for _ in range(n):
    graph.append(list(map(int, input())))

def bfs(x, y):
    q = deque([(x,y)])
    while q:
        a, b = q.popleft()
        for i in range(4):
            X = a + dx[i]
            Y = b + dy[i]
            if X < 0 or X >= n or Y < 0 or Y >= m:
                continue
            if graph[X][Y] == 1:
                graph[X][Y] = graph[a][b] + 1
                q.append((X, Y))


bfs(0,0)
print(graph[n-1][m-1])
# dfs는 재귀의 깊이가 깊어질때, 시간초과가 나올 위험이 크므로, bfs로 푸는것이 시간적 효율이 좋다.