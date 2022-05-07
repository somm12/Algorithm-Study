arr = []
for i in range(9):
    a = int(input())
    arr.append((a,i+1))
arr.sort()

print(arr[8][0])
print(arr[8][1])