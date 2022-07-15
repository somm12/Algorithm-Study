import sys
n = int(input())
stack = list(map(int,sys.stdin.readline().split()))
ans = []
stack2 = []
ans.append(-1)
stack2.append(stack.pop())

while stack:
    val = stack.pop()
    if val < stack2[-1]:
        ans.append(stack2[-1])
        stack2.append(val)
    else:
        while stack2 and val >= stack2[-1] :
            stack2.pop()
        if stack2:
            ans.append(stack2[-1])
        else:
            ans.append(-1)
        stack2.append(val)

ans.reverse()
for val in ans:
    print(val, end = ' ')