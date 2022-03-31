n = int(input())
arr = list(map(int,input()))
result = 0
for i in range(len(arr)):
    result += arr[i]

print(result)