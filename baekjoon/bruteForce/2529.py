import sys
input = sys.stdin.readline
k = int(input())
arr = list(input().split())
res = [0] * (k + 1)
ch = [0] * 10
minV = 1e9 * 10
maxV = -1

def dfs(L, idx):
    global minV, maxV
    if L == k + 1:
        temp = int(''.join(map(str, res))) # 출력시 만약 k+1 길이보다 작으면 앞에 0붙이기
        minV = min(minV, temp)
        maxV = max(maxV, temp)
    else:
        for i in range(10):
            if L == 0:
                ch[i] = 1
                res[L] = i
                dfs(L + 1, idx)
                ch[i] = 0
            elif arr[idx] == '<':
                if res[L - 1] < i and ch[i] == 0:
                    ch[i] = 1
                    res[L] = i
                    dfs(L + 1, idx+1)
                    ch[i] = 0
            elif arr[idx] == '>':
                if res[L - 1] > i and ch[i] == 0:
                    ch[i] = 1
                    res[L] = i
                    dfs(L + 1, idx+1)
                    ch[i] = 0

dfs(0,0)

if len(str(maxV)) < k + 1:
    print('0'+str(maxV))
else:
    print(str(maxV))
if len(str(minV)) < k + 1:
    print('0'+str(minV))
else:
    print(str(minV))