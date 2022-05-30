arr = input().split('-')
answer = 0
#arr[0]는 더하는 부분
for i in arr[0].split('+'):
    answer += int(i)
#arr[1]부터는 다음 - 가 나올 때 까지 더해서 한 번에 빼준다
for k in arr[1:]:
    for j in k.split('+'):
        answer -= int(j)
print(answer)