minV = 100
total = 0
cnt = 0
arr = []
for _ in range(7):
    x = int(input())
    arr.append(x)
    if x % 2 != 0:
        total += x
        minV = min(minV, x)
    else:
        cnt += 1
if cnt == 7:
    print(-1)
else:
    print(total)
    print(minV)
# 홀수인 숫자만 배열에 추가하여 sum, min함수를 이용하는 방법.
import sys

res = []
for _ in range(7):
    a = int(sys.stdin.readline())
    if a % 2 != 0:
        res.append(a)
if len(res) == 7:
    print(sum(res))
    print(min(res))
else:
    print(-1)