def dfs(L):
    if L == n:
        for val in res:
            print(val, end=' ')
        print()
    else:
        for i in range(1, n + 1):
            if ch[i] == 0:
                ch[i] = 1
                res[L] = i
                dfs(L + 1)
                ch[i] = 0
if __name__ == "__main__":
    n = int(input())
    ch = [0] * (n + 1)
    res = [0] * n
    dfs(0)