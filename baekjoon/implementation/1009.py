n = int(input())
answer = []

def findAnswer(num,power):
    value = 1
    repeitionNum = []
    while True:
        value *= num
        value %= 10
        if value == 0:
            value = 10
        if value in repeitionNum:
            break
        else:
            repeitionNum.append(value)
    index = (power % len(repeitionNum)) - 1
    return repeitionNum[index]

for i in range(n):
    a, b = map(int, input().split())
    result = findAnswer(a,b)
    answer.append(result)

for value in answer:
    print(value)