from collections import deque

n, k = map(int, input().split())
MAX = 100000
dist = [0] * (MAX * 2+ 1)

def bfs():
    q = deque([n])
    while q:
        x = q.popleft()
        if x == k:
            print(dist[k])
            exit()
        for nx in [x * 2, x - 1, x + 1]:
            if nx <= 10 ** 5 and nx >= 0 and dist[nx] == 0:
                q.append(nx)
                if nx == 2 * x:
                    dist[nx] = dist[x] + 0
                else:      
                    dist[nx] = dist[x] + 1
bfs()