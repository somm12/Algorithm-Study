import sys

arr = sys.stdin.readline().strip()
arr = list(arr)
reversed_arr = arr[::-1]
if arr == reversed_arr:
    print(1)
else:
    print(0)
