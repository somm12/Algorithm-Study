arr = [0] * 501
arr[1] = 1   

n = int(input())
if n == 0 or n == 1:
    print(0)
    exit(0)

for i in range(2, n + 1):
    arr[i] = arr[i - 1] * i

ans = str(arr[n])
count = 0

for i in range(len(ans) - 1, -1, -1):
    if ans[i] == '0':
        count += 1
    else:
        break
print(count)