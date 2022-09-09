def dfs(L):
    if L == m:
            ans.add(tuple(res))
    else:
        for i in range(n):
            if L == 0 or res[L - 1] <= arr[i]:
                res[L] = arr[i]
                dfs(L + 1)
    
if __name__ == "__main__":
    n, m = map(int,input().split())
    arr = list(set(map(int,input().split())))
    # 중복되는 수를 set으로 감싸서 제거 후, 다시 n을 대입.
    n = len(arr)
    ans = set()
    arr.sort()
    res = [0] * m
    dfs(0)
    ans = list(ans)
    ans.sort()
    for li in ans:
        for v in li:
            print(v, end=' ')
        print()
 