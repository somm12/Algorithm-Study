n = int(input())
data = list(map(int, input().split()))
data.sort()
count = 0

while n != 0:
  max_num = max(data)
  data = data[:n-max_num]
  n -= max_num
  count += 1
print(count)

