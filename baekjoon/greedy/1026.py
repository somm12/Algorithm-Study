n = int(input())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

A.sort()
B.sort(reverse=True)

answer = 0
for index in range(len(A)):
    answer += A[index] * B[index]

print(answer)