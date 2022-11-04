from collections import deque
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
MAX = 100000
dist = [0] * (MAX + 1)

def bfs(n):
    q = deque([n])
    while q:
        x = q.popleft()
        if x == k:
            print(dist[k])
            exit()
        for i in [ x * 2, x - 1, x + 1]:
            if 0 <= i <= MAX and not dist[i]:
                q.append(i)
                if 2 * x == i:
                    dist[i] = dist[x]
                else:
                    dist[i] = dist[x] + 1
bfs(n)