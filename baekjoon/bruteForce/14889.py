import sys
input = sys.stdin.readline

n = int(input())
arr = []
ch = [False] * n
ans = 100000000

def dfs(L, index):
    global ans
    if L == n // 2:
        star = 0
        link = 0
        for i in range(n):
            for j in range(i + 1, n):
                if ch[i] and ch[j]:
                    star += arr[i][j] + arr[j][i]
                elif not ch[i] and not ch[j]:
                    link += arr[i][j] + arr[j][i]
        ans = min(ans, abs(star - link))
    else:
        for i in range(index, n):
            if L == 0 or (not ch[i] and ch[0]):
                ch[i] = True
                dfs(L + 1, i + 1)
                ch[i] = False

for _ in range(n):
    arr.append(list(map(int,input().split())))

dfs(0,0)
print(ans)