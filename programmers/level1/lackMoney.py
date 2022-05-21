def solution(price, money, count):
    answer = 0
    requiredMoney = 0
    for i in range(count):
        requiredMoney += price *(i+1)
    answer = requiredMoney - money
    if answer <= 0:
        answer = 0
    return answer