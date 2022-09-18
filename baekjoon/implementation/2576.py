minV = 100
total = 0
cnt = 0
arr = []
for _ in range(7):
    x = int(input())
    arr.append(x)
    if x % 2 != 0:
        total += x
        minV = min(minV, x)
    else:
        cnt += 1
if cnt == 7:
    print(-1)
else:
    print(total)
    print(minV)