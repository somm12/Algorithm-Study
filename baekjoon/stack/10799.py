import sys
arr = sys.stdin.readline().strip()

stack = []

ans = 0

for i in range(len(arr)):
    if arr[i] == '(':
        stack.append(arr[i])
    else:
        stack.pop()
        if arr[i - 1] == '(':
            ans += len(stack)
        else:
            ans += 1
print(ans)