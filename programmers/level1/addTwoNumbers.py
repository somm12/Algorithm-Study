def solution(numbers):
    answer = []
    for i in range(len(numbers)-1):
        for k in range(i+1,len(numbers)):
            add = numbers[i] + numbers[k]
            if add not in answer:
                answer.append(add)
    answer.sort()
    return answer