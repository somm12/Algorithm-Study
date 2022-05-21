def solution(sizes):
    answer = 0
    bigWidth = [0]
    bigHeight = [0]
    
    for wallet in sizes:
        if wallet[0] < wallet[1]:
            temp = wallet[0]
            wallet[0] = wallet[1]
            wallet[1] = temp
    
    for wallet in sizes:
        bigWidth[0] = max(bigWidth[0],wallet[0])
        bigHeight[0] = max(bigHeight[0],wallet[1])
    
    answer = bigWidth[0] * bigHeight[0]
    return answer