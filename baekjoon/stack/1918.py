from collections import deque
arr = deque(list(input()))

ans = ""
priority = {"*": 1, '/':1, '+':0, '-':0,'(':-1}
stack = []

while arr:
    val = arr.popleft()
    if ord(val) >= 65:
        ans += val
    else:
        if stack:
            if val == '(':
                stack.append(val)
            elif val == ')':
                while stack[-1] != '(':
                    ans += stack.pop()
                stack.pop()
            else:
                while stack:
                    if priority[val] <= priority[stack[-1]]:
                        ans += stack.pop()
                    else:
                        break                
                stack.append(val)
        else:
            stack.append(val)

while stack:
    ans += stack.pop()
for val in ans:
    print(val,end='')            