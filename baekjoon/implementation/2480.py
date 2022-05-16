arr = [0,0,0,0,0,0,0]
dice = list(map(int,input().split()))

for index in range(3):
    arr[dice[index]] += 1

count = 0
for i in arr:
    if i != 0:
        count += 1

if count == 3:
    print(max(dice)*100)
elif count == 2:
    print(1000 + arr.index(2)*100)
elif count == 1:
    print(10000 + arr.index(3)*1000)