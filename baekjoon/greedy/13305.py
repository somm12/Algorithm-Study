from cmath import inf


numOfCity = int(input())
cityDistance = list(map(int,input().split()))
price = list(map(int,input().split()))

result = 0
min = inf
for i in range(numOfCity-1):
    for j in range(i+1):
        if j == i:
            result += price[j] * sum(cityDistance[i:])
        else:
            result += price[j] * cityDistance[j]
    if min > result:
        min = result
    result = 0

print(min)