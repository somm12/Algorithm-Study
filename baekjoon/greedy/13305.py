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

# 그리디 알고리즘은 항상 선택의 순간마다 당장 눈앞에 보이는 최적의 상황만을 쫓아 최종적인 해답을 찾는 알고리즘이다.
# 이 문제에서는 최소 비용을 구하는 것이기 때문에 최소 비용이 되기 위한 조건을 잘 생각하고 정리해서 코드를 짜야한다.
# 최소 비용이 나오려면 우선 리터 당 가격이 싼 도시의 cost를 최대한 사용하면 될 것이다.
# 하지만 최소로 가격이 싼 곳이 첫 번째 도시가 아닐 수 있기 때문에 차근차근 오른쪽으로 도시를 이동하면서
# 더 비용이 적은 도시를 선택해서 계산해 나가면 된다. 그렇게 되면 주어진 상황에서 최선으로 최소 비용을 구할 수 있다.