n = int(input())
info = []
rank = [0 for i in range(n)]

for i in range(n):
   a, b = map(int, input().split())
   info.append((a,b))

for i in range(n):
    for k in range(i+1,n):
        if info[i][0] < info[k][0] and info[i][1] < info[k][1]:
            rank[i] += 1
        elif info[i][0] > info[k][0] and info[i][1] > info[k][1]:
            rank[k] += 1
    rank[i] +=1
for i in range(n):
    print(rank[i], end=' ')
