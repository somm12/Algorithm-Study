def dfs(L):
    if L == m:
            ans.add(tuple(res))
            
    else:
        for i in range(n):
            if ch[i] == 0:
                ch[i] = 1
                res[L] = arr[i]
                dfs(L + 1)
                ch[i] = 0
        
if __name__ == "__main__":
    n, m = map(int,input().split())
    arr = list(map(int,input().split()))
    ans = set()
    arr.sort()
    res = [0] * m
    ch = [0] * n
    dfs(0)
    ans = list(ans)
    ans.sort()
    for li in ans:
        for v in li:
            print(v, end=' ')
        print()
 