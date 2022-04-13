from itertools import count


chass = []
count = 0
for i in range(8):
    row = list(input())
    chass.append(row)

for i in range(8):
    for k in range(8):
        if i % 2 == 0 and k % 2 == 0:
            if chass[i][k] == 'F':
                count += 1
        elif i % 2 == 1 and k % 2 == 1:
            if chass[i][k] == 'F':
                count += 1
print(count)