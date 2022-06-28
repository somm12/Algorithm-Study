n = int(input())
res = []
for i in range(n):
    arr = list(map(int,input().split()))
    total = arr.pop(0)
    totalSum = sum(arr)
    ave = (totalSum // total)
    stu = 0

    for value in arr:
        if value > ave:
            stu += 1
    res.append(((stu/total) * 100))

for k in res:
    print("%.3f"% k+"%")