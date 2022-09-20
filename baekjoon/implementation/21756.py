a = int(input())
arr = [i for i in range(a + 1)]

while True:
    n = len(arr)
    if n == 2:
        break
    for i in range(n):
        if i % 2 == 0:
            arr[i // 2] = arr[i]
    for _ in range(n // 2):
        arr.pop()
print(arr[1])