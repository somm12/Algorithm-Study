from collections import deque
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int,input())))
ans = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def sol(x,y):
    count = 1
    graph[x][y] = 0
    queue = deque([(x,y)])
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            X = a + dx[i]
            Y = b + dy[i]
            if X < 0 or X >= n or Y < 0 or Y >= n:
                continue
            if graph[X][Y] == 1:
                queue.append((X, Y))
                graph[X][Y] = 0
                count += 1
    return count

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            ans.append(sol(i, j))

ans.sort()
print(len(ans))
for i in ans:
    print(i)

