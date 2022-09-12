n = int(input())
arr = list(map(int, input().split()))

for i in range(n - 1, 0, -1):
    if arr[i] < arr[i - 1]:
        x = i - 1
        y = i
        for j in range(n - 1, 0, -1):
            if arr[x] > arr[j]:
                arr[x], arr[j] = arr[j], arr[x]
                new = arr[:y] + sorted(arr[y:], reverse=True)
                for val in new:
                    print(val, end=' ')
                exit()
print(-1)