n = int(input())
inf = float("inf")
result = inf
for i in range(0,(n//3)+1):
    y = (-3/5)*i + (n/5)
    k = i + y
    if k % 1 > 0:
        k = inf
    result = min(result, k)

if result >= inf:
    result = -1

print(int(result))

#default value was the reason why I was wrong.