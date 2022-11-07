from glob import glob


n = int(input())
num = list(map(int, input().split()))
a = list(map(int, input().split()))
nonum = []
minV = 10 ** 9
maxV  = -(10 ** 9)
ch = [0] * (n - 1)
order = []

for i in range(4):
    if i == 0:
        for i in range(a[i]):
            nonum.append('+')
    elif i == 1:
        for i in range(a[i]):
            nonum.append('-')
    elif i == 2:
        for i in range(a[i]):
            nonum.append('x')
    else:
        for i in range(a[i]):
            nonum.append('/')
def sol():
    ans = num[0]
    for i in range(n - 1):
        if order[i] == '+':
            ans = ans + num[i + 1]
        elif order[i] == '-':
            ans = ans - num[i + 1]
        elif order[i] == 'x':
            ans = ans * num[i + 1]
        elif order[i] == '/':
            if ans < 0:
                ans = ans * -1
                ans = ans // num[i + 1]
                ans = ans * -1
            else:
                ans = ans // num[i + 1]
    return ans

def dfs(L):
    global minV, maxV
    if L == n - 1:
        v = sol()
        minV = min(minV, v)
        maxV = max(maxV, v)
        return
    else:
        for i in range(n - 1):
            if ch[i] == 0:
                order.append(nonum[i])
                ch[i] = 1
                dfs(L + 1)
                ch[i] = 0
                order.pop()

dfs(0)
print(maxV)
print(minV)