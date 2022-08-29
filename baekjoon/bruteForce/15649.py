def dfs(L):
    if L == m:
        for j in range(L):
            print(res[j],end=' ')
        print()
    else:
        for i in range(1, n+1):
            if ch[i] == 0:
                ch[i] = 1
                res[L] = i
                dfs(L+1)
                ch[i] = 0

if __name__ == "__main__":
    n, m = map(int,input().split())
    res = [0] * n
    ch = [0] * (n + 1)
    dfs(0)