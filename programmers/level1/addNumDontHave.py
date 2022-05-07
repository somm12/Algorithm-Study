def solution(numbers):
    answer = 0
    for i in arr:
        if i not in numbers:
            answer += i
    return answer

arr = [i for i in range(1,10)]
print(arr)