import sys
arr = sys.stdin.readline().rstrip()
c1 = 0
c2 = 0
ans = ""
stack = list()
for val in arr:
    if val == "<":
        c1 += 1
        while stack:
            ans += stack.pop()
        ans += val
    elif val == ">":
        c2 += 1
        ans += val
    elif c1 != c2:
        ans += val
    elif val == " ":
        while stack:
            ans += stack.pop()
        ans += val
    else:
        stack.append(val)

while stack:
    ans += stack.pop()
print(ans)