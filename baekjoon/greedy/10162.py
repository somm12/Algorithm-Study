T = int(input())

arr = [300,60,10]

count = []

for time in arr:
    count.append(T//time)
    T = T % time

if T != 0:
    print(-1)
else:
    for i in count:
        print(i, end=' ')