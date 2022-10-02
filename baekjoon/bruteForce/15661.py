import sys
input = sys.stdin.readline

n = int(input())
s = []
ch = [0] * n
ans = 100000000
for _ in range(n):
    s.append(list(map(int,input().split())))

def dfs(depth, L, index):
    global ans
    if L == depth:
        star = 0
        link = 0
        for i in range(n):
            if ch[i] == 1:
                for j in range(i + 1, n):
                    if ch[j] == 1:
                        star += s[i][j] + s[j][i]
            else:
                for j in range(i + 1, n):
                    if ch[j] == 0:
                        link += s[i][j] + s[j][i]
        ans = min(ans, abs(star - link))
        if ans == 0:
            return
        return
    for i in range(index, n):
        if ch[i] == 0:
            ch[i] = 1
            dfs(depth , L + 1, i + 1)
            ch[i] = 0

for d in range(n//2,0,-1):
    dfs(d, 0, 0)
    if ans == 0:
        break
print(ans)