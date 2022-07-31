index1 = 0
index2 = 0
arr = []
for _ in range(9):
    arr.append(int(input()))
arr.sort()
total = sum(arr)

for i in range(len(arr)):
    for k in range(i + 1, len(arr)):
        if total - (arr[i] + arr[k]) == 100:
            index1 = i
            index2 = k
            break
for i in range(len(arr)):
    if i != index1 and i != index2:
        print(arr[i])