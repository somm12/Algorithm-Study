from collections import deque


n = int(input())
graph = []
ans = []

for _ in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0,0, -1,1]

def BFS(x, y):
    count = 1
    q = deque([(x,y)])
    graph[x][y] = 0
    while q:
        a, b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx, ny))
                count += 1
    return count

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            ans.append(BFS(i,j))
ans.sort()
print(len(ans))
for i in ans:
    print(i)