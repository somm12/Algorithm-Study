from glob import glob
import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
maxV = -1
res = 0

def sol(x):
    global maxV,res
    if len(arr) == 2:
        maxV = max(x, maxV)
        return
    else:
        for i in range(1, len(arr) - 1):
            res = arr[i-1] * arr[i+1]
            v = arr.pop(i)
            sol(x + res)
            arr.insert(i,v)

sol(0)
print(maxV)
# 누적해서 더하는 것이 있다면, 매개변수를 이용한다.
# pop, insert를 이용해 특정 index 의 값을 빼고 삽입가능하다.