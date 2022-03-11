test_case = int(input())
result = []
new_S = ''
for i in range(test_case):
    R, S = input().split()
    R = int(R)
    for k in range(len(S)):
        new_S += S[k]*R
    result.append(new_S)
    new_S = ''

for value in result:
    print(value)