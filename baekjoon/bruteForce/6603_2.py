def dfs(L):
    if L == 6:
        for i in res:
            print(i, end=' ')
        print()
    else:
        for i in range(k):
            if L == 0 or (ch[i] == 0 and res[L - 1] < arr[i]):
                ch[i] = 1
                res.append(arr[i])
                dfs(L + 1)
                ch[i] = 0
                res.pop()
while True:
    arr = list(map(int, input().split()))    
    k = arr[0]
    if k == 0:
        exit()
    arr = arr[1:]
    ch = [0] * k
    res = []
    dfs(0)
    print()