from collections import deque
n = int(input())
arr = []
check = []
for i in range(n):
    arr.append(int(input()))

arr.sort()
arr = deque(arr)
for i in range(n):
    m = len(arr)
    temp = arr.popleft()
    check.append(temp * m)

print(max(check))