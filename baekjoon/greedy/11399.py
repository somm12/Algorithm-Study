N = int(input())
arr = list(map(int,input().split()))

arr.sort()

answer = 0
result = 0
for i in arr:
    result += i
    answer += result
print(answer)