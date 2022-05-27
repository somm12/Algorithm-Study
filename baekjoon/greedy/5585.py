money = int(input())

target = 1000 - money

coins = [500,100,50,10,5,1]
count = 0
for coin in coins:
    if target >= coin:
        count += target // coin
        target = target % coin

print(count)