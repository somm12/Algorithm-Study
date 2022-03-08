N = int(input())
money = []
Sum = 0

for i in range(N):
    value = int(input())
    if value != 0:
        money.append(value)
    elif value == 0 and i > 0:
        del(money[-1])
        

for value in money:
    Sum += value
print(Sum)
