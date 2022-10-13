from collections import deque
dx = [1,-1,0,0,1,1,-1,-1]
dy = [0,0,-1,1,-1,1,-1,1]

def sol(graph, i, j, w, h):
    graph[i][j] = 0
    q = deque([(i, j)])
    while q:
        a, b = q.popleft()
        for i in range(8):
            x = a + dx[i]
            y = b + dy[i]
            if x < 0 or x >= h or y < 0 or y >= w:
                continue
            if graph[x][y] == 1:
                q.append((x,y))
                graph[x][y] = 0

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        exit()
    graph = []
    count = 0
    for _ in range(h):
        graph.append(list(map(int, input().split())))
    
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                sol(graph,i,j,w,h)
                count += 1
    print(count)
        