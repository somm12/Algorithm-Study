from ctypes import BigEndianStructure


def dfs(w, p, t):
    global total

    if t == 24:
        total = max(total,w)
        return
    if p > m:
        return
    if p < 0:
        p = 0

    dfs(w + b, p + a, t + 1)
    dfs(w, p - c , t + 1)

a, b, c, m = map(int,input().split())
total = -1
dfs(0,0,0)
print(total)