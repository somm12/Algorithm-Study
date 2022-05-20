def solution(n):
    answer = 0
    reversedThree = []
    while n != 0:
        reversedThree.append(n%3)
        n = n // 3
    power = 0
    for i in reversed(range(len(reversedThree))):
        cal = reversedThree[i] * (3**power)
        answer += cal
        power += 1
    return answer

