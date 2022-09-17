def dfs(L):
    if L == n:
        cnt = 0
        for v in nes:
            if v in res:
                cnt += 1
        #모음이 1개라도 존재, 자음도 2개이상 존재. => 이런 조건이 있다면 숫자로 해결하자. 놓치면 경우가 있다.
        if cnt > 0 and n - cnt >= 2:
            for val in res:
                print(val,end='')
            print()      

    else:
        for i in range(C):
            if ch[i] == 0:
                if (L == 0) or (res[L - 1] < arr[i]):
                    ch[i] = 1
                    res[L] = arr[i]
                    dfs(L + 1)
                    ch[i] = 0

n, C = map(int, input().split())
arr = list(input().split())
arr.sort()
res = [0] * n
ch = [0] * C
nes = ['a','e','i','o','u']
dfs(0)