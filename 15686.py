n,M = map(int, input().split())
arr = [[0]*n for i in range(n)]

chicken=[]
house=[]

for i in range(n):
  a = list(map(int, input().split()))
  arr[i]= a

for i in range(n):
  for k in range(n):
    value = arr[i][k]
    if value == 2:
      chicken.append((i+1,k+1))
    if value == 1:
      house.append((i+1,k+1))

chicken_distance = []

val = 0
for i in range(len(chicken)):
    for k in range(len(house)):
        add = abs(chicken[i][0]-house[k][0]) + abs(chicken[i][1]-house[k][1])
        val += add
    chicken_distance.append((val,i))
    val = 0

chicken_distance.sort()

chicken_distance = chicken_distance[:M]


last_chicken = []
for i in range(len(chicken_distance)):
    
    last_chicken.append(chicken[chicken_distance[i][1]])


#sum of all the distances between chicken stores and houses
result = 0
find_min_value= []
for i in range(len(house)):
  for k in range(len(last_chicken)):
    add = abs(house[i][0]-last_chicken[k][0]) + abs(house[i][1]-last_chicken[k][1])
    find_min_value.append(add)
  result+=min(find_min_value)
  find_min_value = []

print(result)
