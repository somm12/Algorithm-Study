n, k = map(int,input().split())
coin = []
for _ in range(n):
    coin.append(int(input()))
coin.sort(reverse=True)
count = 0
for i in range(n):
    count += (k // coin[i])
    k = k % coin[i]
print(count)