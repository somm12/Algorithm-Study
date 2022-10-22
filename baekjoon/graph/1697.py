from collections import deque

n, k = map(int, input().split())

def bfs():
    q = deque([n])
    while q:
        v  = q.popleft()
        if v == k:
            print(dist[v])
            break
        for nx in (v - 1, v + 1, v * 2):
            if nx >= 0 and nx <= 10 ** 5 and not dist[nx]:
                q.append(nx)
                dist[nx] = dist[v] + 1
dist = [0] * (10**5 + 1)
bfs()

# 아래는 메모리 초과 코드.
# def bfs():
#     q = deque([(n,0)])
#     while q:
#         v ,length = q.popleft()
#         if v == k:
#             print(length)
#             break
#         for nx in (v - 1, v + 1, v * 2):
#             if nx >= 0 and nx <= 10 ** 5:
#                 q.append((nx,length + 1))