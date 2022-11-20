import sys
input = sys.stdin.readline

n = int(input())
c = []
for _ in range(n):
    c.append(list(map(int, input().split())))
c.sort(key=lambda x:x[0])
c.sort(key=lambda x:x[1])

count = 0
temp = 0

for v in c:
    if v[0] >= temp:
        count += 1
        temp = v[1]
print(count)

#개수를 셀 때, 1부터 센다면, 그 이후부터 검사를 해야한다. 주관이 포함되면 안됨.