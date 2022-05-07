def solution(survey, choices):
    kinds = ['R','T','C','F','J','M','A','N']
    score = [0,0,0,0,0,0,0,0]
    answer = ''
    # 점수 매기기
    for question in survey:
        #약간 동의 / 약간 비동의
        if choices[survey.index(question)] == 5:
            score[kinds.index(question[1])] += 1
        elif choices[survey.index(question)] == 3:
            score[kinds.index(question[0])] += 1
        #매우 동의 / 매우 비동의
        elif choices[survey.index(question)] == 7:
            score[kinds.index(question[1])] += 3
        elif choices[survey.index(question)] == 1:
            score[kinds.index(question[0])] += 3
        # 동의 / 비동의
        elif choices[survey.index(question)] == 6:
            score[kinds.index(question[1])] += 2
        elif choices[survey.index(question)] == 2:
            score[kinds.index(question[0])] += 2
        survey[survey.index(question)] = "done"
    # 각 유형 점수 비교  
    for i in range(0,len(score),2):
        if score[i] > score[i+1]:
            answer += kinds[i]
        elif score[i] < score[i+1]:
            answer += kinds[i+1]
        else:# 같은 점수일 때 사전 순.
            if ord(kinds[i]) < ord(kinds[i+1]):
                answer += kinds[i]
            else:
                answer += kinds[i+1]
    return answer