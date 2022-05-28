n = int(input())
meeting = []

for i in range(n):
    meeting.append(list(map(int,input().split())))

meeting.sort(key = lambda x:(x[1],x[0]))

count = 0
et = 0
for s, e in meeting:
    if s >= et:
        et = e
        count += 1

print(count)
