n,m = map(int , input().split())
result = []
for i in range(n):
    row = list(map(int, input().split()))
    row.sort()
    result.append(row[0])
result.sort()
print(result[n-1])

#you can use min() & max()