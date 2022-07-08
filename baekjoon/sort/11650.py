n = int(input())
arr = []
for _ in range(n):
    a, b = map(int,input().split())
    arr.append((a,b))
arr.sort()

for a,b in arr:
    print(a,b)