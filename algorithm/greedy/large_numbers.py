# n, m, k = map(int, input().split())
# data = list(map(int, input().split()))
# print(data)

# data.sort()
# first = data[n-1]
# second = data[n-2]

# result = 0
# result += (k*first+second)*(m//(k+1))
# if (m%(k+1)) > 0:
#   result += (m%k)*first
# print(result)
# 2 번
# n, m = map(int, input().split())
# arr = []
# for i in range(0,n):
#   data = list(map(int, input().split()))
#   arr.append(min(data))
# arr.sort()
# print(arr[n-1])
# 3번
n, k = map(int, input().split())
count = 0
while n != 1:
  if n%k != 0:
    n = n - 1
    count += 1
  else:
    n = n//k
    count += 1
print(count)