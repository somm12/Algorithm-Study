n = int(input())
carNumber = list(map(int,input().split()))
answer = 0
for number in carNumber:
    if number == n:
        answer += 1

print(answer)