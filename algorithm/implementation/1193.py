import sys

n = int(sys.stdin.readline())
arr = []
Sum = 0
limit = 0
for i in range(1,n+1):
    Sum += i
    if Sum >= n:
        limit = i
        break



if (limit%2 == 1):
    k = limit
    for i in range(1,limit+1):
        arr.append(str(k)+'/'+str(i))
        k -= 1
else:
    k = limit
    for i in range(1,limit+1):
        arr.append(str(i)+'/'+str(k))
        k -= 1
print(arr[n-Sum-1])      