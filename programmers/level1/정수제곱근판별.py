def solution(n):
    answer = -1
    for x in range(1, int(n ** 0.5) + 1):
        if x ** 2 == n:
            answer = (x + 1) ** 2

    return answer
# 아래는 더 생각해본 더 빠른 코드 
def solution(n):
    answer = -1
    temp = n ** 0.5 
    # 11.0 == 11 즉 제곱근 한 수는 float가 나오는데 이 수가 정수인지 판별.
    # 아니라면, 제곱근이 없는 것.
    if int(temp) == temp:
        answer = (int(temp) + 1) ** 2
        return answer

    return answer