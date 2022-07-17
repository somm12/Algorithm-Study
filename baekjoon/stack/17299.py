from re import L
import sys
n = int(sys.stdin.readline())
stack = list(map(int,sys.stdin.readline().split()))
counting = [0] * 1000001
stack2 = []
ans = []

for i in stack:
    counting[i] += 1

for i in range(len(stack)):
    stack[i] = (stack[i], counting[stack[i]])
ans.append(-1)
stack2.append(stack.pop())

while stack:
    val = stack.pop()
    if val[1] < stack2[-1][1]:
        ans.append(stack2[-1][0])
        stack2.append(val)
    else:
        while stack2 and val[1] >= stack2[-1][1]:
            stack2.pop()
        if stack2:
            ans.append(stack2[-1][0])
        else:
            ans.append(-1)
        stack2.append(val)
ans.reverse()

for k in ans:
    print(k, end=' ')