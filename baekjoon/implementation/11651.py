import sys
n = int(sys.stdin.readline())
arr = []
for i in range(n):
    a = list(map(int,input().split()))
    a.reverse()
    arr.append(a)
arr.sort()
for value in arr:
    value.reverse()
    print("%d %d"%(value[0],value[1]))
