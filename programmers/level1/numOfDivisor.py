def solution(left, right):
    answer = 0
    result = []
    count = 0
    for i in range(left,right+1):
        for k in range(1,i+1):
            if i % k == 0:
                count += 1
        if count % 2 == 0:
            result.append(i)
        else:
            result.append(-i)
        count = 0
    
    for i in result:
        answer += i
    return answer