import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    count = 0
    for i in range(1, n):
        for j in range(i + 1, n):
           if (i*i + j*j + m) % (i*j) == 0:
               count += 1
    print(count)