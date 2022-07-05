def DFS(L,sum):
    global res,max,arr
    if L == 3:
        if max < sum and sum <= m:
            max = sum
    else:
        for i in arr:
            if i not in res:
                res.append(i)
                DFS(L + 1, sum + i)
                res.pop()

if __name__ == "__main__":
    res = []
    max = -1
    n, m = map(int,input().split())
    arr = list(map(int,input().split()))
    DFS(0,0)
    print(max)