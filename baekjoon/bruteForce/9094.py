import sys
input = sys.stdin.readline
output = sys.stdout.write
T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    count = 0
    for i in range(1, n):
        for j in range(i + 1, n):
            temp = i ** 2 + j ** 2 + m
            temp2 = i * j
            res = temp / temp2
            if res == int(res):
                count += 1
    output(str(count))