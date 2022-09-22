def solution(n):
    answer = 0
    while n > 0:
        answer += n % 10
        n = n // 10
    return answer

def solution(n):
    if n < 10:
        return n
    return n % 10 + solution(n // 10)