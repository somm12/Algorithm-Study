def solution(s):
    numP = 0
    numY = 0
    for i in s:
        if i == 'P' or i == 'p':
            numP += 1
        elif i == 'Y' or i == 'y':
            numY += 1
    if numP == numY:
        return True
    return False

# 빠른풀이
# return s.lower().count('p') == s.lower().count('y')