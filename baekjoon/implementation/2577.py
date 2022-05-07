A = int(input())
B = int(input())
C = int(input())

result = A*B*C
result = str(result)

arr = [0 for i in range(10)]

for value in result:
    
    arr[int(value)] += 1

for a in arr:
    print(a)