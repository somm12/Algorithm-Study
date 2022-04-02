n = int(input())
score = list(map(int,input().split()))
Sum=0
maxScore = max(score)
for i in range(n):
    score[i] = (score[i]/maxScore)*100
    Sum += score[i]

print(Sum/n)