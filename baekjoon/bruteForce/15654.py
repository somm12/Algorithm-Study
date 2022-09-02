def dfs(L):
    if L == m:
        for val in res:
            print(val, end=' ')
        print()
    else:
        for i in range(n):
            if arr[i] not in res[:L]:
                res[L] = arr[i]
                dfs(L + 1)
if __name__ == "__main__":
    n, m = map(int,input().split())
    arr = list(map(int,input().split()))
    arr.sort()
    res = [0] * m
    dfs(0)