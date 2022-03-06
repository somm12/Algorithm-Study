n = list(input())

numOfZero = 0
numOfOne = 0
duplicateZero=0
duplicateOne = 0
length = len(n)

for i in range(length):
    if n[i] == '0':
        numOfZero += 1

    else:
        numOfOne += 1

if numOfZero <= numOfOne:
    for i in range(length):
        if n[i] == '0':
            for i in range(i+1, length):
                if(n[i] == '0'):
                    duplicateZero += 1
                else:
                    break

if numOfZero > numOfOne:
    for i in range(length):
        if n[i] == '1':
            for i in range(i+1, length):
                if(n[i] == '1'):
                    duplicateOne += 1
                else:
                    break

a = numOfZero - duplicateZero
b = numOfOne - duplicateOne
print(min(a,b))
