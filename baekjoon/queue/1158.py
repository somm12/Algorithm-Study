from collections import deque

arr = deque()
ans = []

n, k = map(int,input().split())

for i in range(1, n + 1):
    arr.append(i)

while arr:
    for i in range(1, k + 1):
        val = arr.popleft()
        if i != k:
            arr.append(val)
        else:
            ans.append(val)
print("<"+', '.join(map(str,ans))+">")
