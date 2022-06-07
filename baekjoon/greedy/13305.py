from cmath import inf


numOfCity = int(input())
cityDistance = list(map(int,input().split()))
cost = list(map(int,input().split()))

result = 0
lowerCost = inf

for i in range(numOfCity - 1):
    if cost[i] < lowerCost:
        result += cost[i] * cityDistance[i]
        lowerCost = cost[i]
    else:
        result += lowerCost * cityDistance[i]
print(result)