import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
maxV = -1
def sol(ans):
    global maxV
    if len(arr) == 2:
        maxV = max(maxV, ans)
        return
    for i in range(1, len(arr) - 1):
        temp = arr[i - 1] * arr[i + 1]
        a = arr.pop(i)
        sol(ans + temp)
        arr.insert(i, a)
sol(0)
print(maxV)