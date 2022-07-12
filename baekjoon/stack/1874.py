import sys
input = sys.stdin.readline
n = int(input())
arr1 = []
arr2 = []
res = []
ans = []
arr1Index = 0
arr2Element = 1

for _ in range(n):
    arr1.append(int(input()))

while arr2Element <= n:
    if arr1[arr1Index] in arr2:
        res.append(arr2.pop())
        ans.append("-")
    else:
        for k in range(arr2Element, arr1[arr1Index] + 1):
            arr2.append(k)
            ans.append("+")
            arr2Element += 1
        res.append(arr2.pop())
        ans.append("-")
    arr1Index += 1

while len(arr2) > 0:
    res.append(arr2.pop())
    ans.append("-")
if res != arr1:
    print("NO")
else:
    for val in ans:
        print(val)