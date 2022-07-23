ans = []
arr = input()

for i in range(len(arr)):
    ans.append(arr[i:len(arr)])

ans.sort()

for val in ans:
    print(val)