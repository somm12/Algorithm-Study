def solution(n):
    answer = []
    while n > 0:
        answer.append(n % 10)
        n = n // 10
    return answer
# 더 간단한 방법.
def solution(n):
    return list(map(int, reversed(str(n))))