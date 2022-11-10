from glob import glob
import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
maxV = -1
add = 0

def sol(x):
    global maxV
    if len(arr) == 2:
        maxV = max(x, maxV)
        return
    else:
        for i in range(1, len(arr) - 1):
            add = arr[i-1] * arr[i+1]
            v = arr.pop(i)
            sol(x + add)
            arr.insert(i,v)

sol(0)
print(maxV)