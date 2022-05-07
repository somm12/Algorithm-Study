import sys
while True:
    arr = sys.stdin.readline().strip()
    if int(arr) == 0:
        break
    arr = list(arr)
    reversed_arr = arr[::-1]
    if arr == reversed_arr:
        print("yes")
    else:
        print("no")
#baekjoon algorithm 1259.py