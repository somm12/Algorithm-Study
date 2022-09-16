def dfs(L):
    if L == 6:
        for val in res:
            print(val, end =' ')
        print()
    else:
        for i in range(k):
            if (visited[i] == 0 and res[L - 1] < s[i]) or L == 0:
                visited[i] = 1
                res[L] = s[i]
                dfs(L + 1)
                visited[i] = 0
while True:
    arr = list(map(int, input().split()))
    s = arr[1:]
    k = arr[0]
    res = [0] * 6
    visited = [0] * k
    if k == 0:
        exit()
    dfs(0)
    print()