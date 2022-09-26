import sys
input = sys.stdin.readline

def dfs(total):
    global count
    if total > n:
        return
    elif total == n:
        count += 1
    else:
        for i in range(1,4):
            dfs(total + i)

t = int(input())
for i in range(t):
    n = int(input())
    count = 0
    dfs(0)
    print(count)