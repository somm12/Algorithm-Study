import sys
from itertools import permutations

n = int(input())
num = list(map(int, input().split()))
a = list(map(int, input().split()))
ops = []
minV = 10 ** 9
maxV  = -(10 ** 9)
ch = [0] * (n - 1)
order = []

minV = sys.maxsize
maxV = -1 * sys.maxsize

for i in range(4):
    for k in range(a[i]):
        ops.append(i)
# ops에는 연산자 개수만큼 해당 인덱스가 들어감. 0 2 1 0 => ops: 1 1 2.

for com in set(permutations(ops, n-1)):
    answer = num[0]
    for i in range(len(com)):
        if com[i] == 0:
            answer += num[i+1]
        elif com[i] == 1:
            answer -= num[i+1]
        elif com[i] == 2:
            answer *= num[i+1]
        else:
            # 부호가 음수면.
            if answer < 0:
                answer = -1 * (abs(answer) // abs(num[i+1]))
            else:
                answer = answer//num[i+1]

    minV = min(minV, answer)
    maxV = max(maxV, answer)

print(maxV)
print(minV)