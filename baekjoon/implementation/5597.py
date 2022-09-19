import sys
input = sys.stdin.readline
ch = [0] * 31

for _ in range(28):
    n = int(input())
    ch[n] = 1
for i in range(1,31):
    if ch[i] == 0:
        print(i)