answer = []
for i in range(3):
    arr = list(map(int,input().split()))
    count = 0
    for element in arr:
        if element == 0:
            count += 1
    if count == 1:
        answer.append('A')
    elif count == 2:
        answer.append('B')
    elif count == 3:
        answer.append('C')
    elif count == 4:
        answer.append('D')
    else:
        answer.append('E')

for i in answer:
    print(i)