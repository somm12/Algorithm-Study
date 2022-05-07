hex_num = list(input())
hex_num.reverse()

def trans(num):
    if num =='A':
        return 10
    elif num == 'B':
        return 11
    elif num == 'C':
        return 12
    elif num == 'D':
        return 13
    elif num == 'E':
        return 14
    elif num == 'F':
        return 15
    else:
        return int(num)
result = 0
for i in range(len(hex_num)):
    result += 16**i * trans(hex_num[i])
print(result)