# from collections import deque

# n, k = map(int, input().split())

# def bfs():
#     q = deque([n])
#     while q:
#         v  = q.popleft()
#         if v == k:
#             res[k].append(k)
#             print(dist[k])
#             for i in res[k]:
#                 print(i, end=' ')
#             break
#         for nx in (v - 1, v + 1, v * 2):
#             temp = []
#             if nx >= 0 and nx <= 10 ** 5 and not dist[nx]:
#                 q.append(nx)
#                 temp = res[v][:] # 참조 없이
#                 temp.append(v)
#                 res[nx] = temp
#                 dist[nx] = dist[v] + 1
# dist = [0] * (10**5 + 1)
# res = [[]] * (10**5 + 1)
# bfs()

from collections import deque

n, k = map(int, input().split())
dist = [0] * (10**5 + 1)
path = [0] * (10**5 + 1)
def show_path(x):
    arr = []
    temp = x
    for _ in range(dist[x] + 1):
        arr.append(temp)
        temp = path[temp]
    for i in arr[::-1]:
        print(i, end=' ')

def bfs():
    q = deque([n])
    while q:
        v  = q.popleft()
        if v == k:
            print(dist[k])
            show_path(k)
            break
        for nx in (v - 1, v + 1, v * 2):
            if nx >= 0 and nx <= 10 ** 5 and not dist[nx]:
                q.append(nx)
                path[nx] = v
                dist[nx] = dist[v] + 1

bfs()