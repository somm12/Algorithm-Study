from collections import deque


n = int(input())
d = [[-1] * (n+1) for _ in range(n+1)]

def sol():
    q = deque([(1,0)])
    d[1][0] = 0
    while q:
        s, c = q.popleft()
        if s == n:
            print(d[s][c])
            exit()
        if s <= n and d[s][s] == -1:
            d[s][s] = d[s][c] + 1
            q.append((s, s))
        if s+c <= n and d[s+c][c] == -1:
            d[s+c][c] = d[s][c] + 1
            q.append((s + c, c))
        if s - 1 >=0 and d[s-1][c] == -1:
            d[s-1][c] = d[s][c] + 1
            q.append((s-1, c))
sol()
