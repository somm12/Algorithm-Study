from collections import deque
import sys
n = int(input())
arr =list(sys.stdin.readline().rstrip())
arr = deque(arr)
alpha = [0] * 27
stack = []

for i in range(1, n + 1):
    alpha[i] = int(input())

while arr:
    val = arr.popleft()
    if ord(val) < 65:
        b = stack.pop()
        a = stack.pop()
        if val == '+':
            stack.append(a + b)
        elif val == '-':
            stack.append(a - b)
        elif val == '*':
            stack.append(a * b)
        else:
            stack.append(a / b)
    else:
        index = ord(val) - 64
        stack.append(alpha[index])
print("%.2f" % stack[-1])