import sys
input = sys.stdin.readline

arr = set()
n = int(input())

for _ in range(n):
    a = input()
    arr.add((len(a), a))
arr = list(arr)
arr.sort()

for a, b in arr:
    print(b, end='')