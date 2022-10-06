import sys
input = sys.stdin.readline
n = int(input())
ch = [False] * n
s = []
total = 1e9
for _ in range(n):
    s.append(list(map(int,input().split())))

def dfs(L, next):
    global total
    if L == n//2:
        star = 0
        link = 0
        for i in range(n):
            for j in range(i + 1, n):
                if ch[i] and ch[j] :
                    star += s[i][j] + s[j][i]
                elif not ch[i] and not ch[j]:
                    link += s[i][j] + s[j][i]
        total = min(total, abs(star - link))
        if total == 0:
            print(total)
            exit()
        return
    for i in range(next, n):
        if L == 0 or (not ch[i] and ch[0]):
            ch[i] = True
            dfs(L + 1, i + 1)
            ch[i] = False
dfs(0,0)
print(total)