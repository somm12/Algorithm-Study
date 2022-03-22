n = int(input())

for i in range(n):
    arr = list(input())
    count = 0
    a = []
    for k in range(len(arr)):
        if arr[k] != 'X':
            count +=1
            a.append(count)
        else:
            count = 0
    result = 0
    for s in range(len(a)):
        result += a[s]
    print(result)
    
        