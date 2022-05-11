from queue import Empty


answer = []
index = 0

N , K = map(int, input().split())
arr = [i for i in range(1,N+1)]

index = index + K - 1

num = arr.pop(index)
answer.append(num)

while len(arr) != 0:
    index += (K - 1)
    while index >= len(arr):
        index = index - len(arr)
    num =  arr.pop(index)
    answer.append(num)

print('<',end='')
for i in range(len(answer)):
    if i == N - 1:
        print(answer[i],end='>')
    else:
        print(answer[i],end=', ')