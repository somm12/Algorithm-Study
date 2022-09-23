
def solution(x):
    answer = 0
    temp = x
    while temp > 0:
        answer += temp % 10
        temp = temp // 10
    
    res = x % answer
    if res == 0:
        return True
    
    return False
# 빠른 풀이
# return n % sum([int(c) for c in str(n)]) == 0