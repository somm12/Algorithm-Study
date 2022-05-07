def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        if signs[i] == True:
            sign = 1
        else:
            sign = -1
        answer += (absolutes[i]*sign)
    return answer