maxNum = 0
result = 0
for i in range(4):
    a , b = map(int,input().split())
    result -= a
    result += b
    maxNum = max(result,maxNum)
print(maxNum)
    