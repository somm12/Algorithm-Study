import sys
input = sys.stdin.readline

def dfs(n):
    if n == L:
        cnt = 0
        for i in res:
            if i in alpha:
                cnt += 1#모음개수 세기
        if cnt >= 1 and L - cnt >= 2:
            for i in res:
                print(i, end='')
            print()
    else:
        for i in range(C):
            if n == 0 or (ch[i] == 0 and arr[i] > res[n - 1]):
                ch[i] = 1
                res[n] = arr[i]
                dfs(n + 1)
                ch[i] = 0
L, C = map(int, input().split())
arr = list(input().split())
arr.sort()
ch = [0] * C
res = [0] * L
alpha = ['a','e','i','o','u']
dfs(0)