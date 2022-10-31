
k = int(input())
comp = list(input().split())

minV = 10**10
maxV = -1
visited = [0] * 10
res = [0] * (k + 1)

def sol(L):
    global minV, maxV
    if L == k + 1:
        ans = ''
        for i in res:
            ans += str(i)
        minV = min(minV, int(ans))
        maxV = max(maxV, int(ans))
        return
    for i in range(10):
        if visited[i] == 0:
            if L == 0:
                visited[i] = 1
                res[L] = i
                sol(L + 1)
                visited[i] = 0
            elif comp[L - 1] == '<' and res[L - 1] < i:
                visited[i] = 1
                res[L] = i
                sol(L + 1)
                visited[i] = 0
            elif comp[L - 1] == '>' and res[L - 1] > i:
                visited[i] = 1
                res[L] = i
                sol(L + 1)
                visited[i] = 0
sol(0)



if len(str(maxV)) < k + 1:
    print('0'+str(maxV))
else:
    print(maxV)
if len(str(minV)) < k + 1:
    print('0'+str(minV))
else:
    print(minV)