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
            for j in range(i + 1, n):
                if ch[i] == 1 and ch[j] == 1:
                    star += s[i][j] + s[j][i]
                elif ch[i] == 0 and ch[j] == 0:
                    link += s[i][j] + s[j][i]
        if depth == 1:
            ans = min(ans, link)
        else:
            ans = min(ans, abs(star - link))
    else:
        for i in range(index, n):
            if ch[i] == 0:
                ch[i] = 1
                dfs(depth , L + 1, i + 1)
                ch[i] = 0

for d in range(1, n//2 + 1):
    dfs(d, 0, 0)
print(ans)