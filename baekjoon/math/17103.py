arr = [True] * 1000001

for i in range(2, 1001):
    if arr[i]:
        for k in range(i + i, 1000001, i):
            arr[k] = False

T = int(input())
count = 0
for _ in range(T):
    n = int(input())
    for i in range(2, n//2 + 1):
        if arr[i] and arr[n - i]:
            count += 1
    print(count)
    count = 0