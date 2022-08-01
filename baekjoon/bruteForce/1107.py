import sys
input = sys.stdin.readline
target = int(input())
n = int(input())
if n > 0:
    broken = list(map(int,input().split()))
else:
    minCount = abs(100 - target)
    minCount = min(minCount, len(str(target)))
    print(minCount)
    exit(0)
minCount = abs(100 - target)

for num in range(1000001):
    num = str(num)

    for i in range(len(num)):
        if int(num[i]) in broken:
            break
        elif i == len(num) - 1:
            minCount = min(minCount, abs(int(num) - target) + len(num))
print(minCount)