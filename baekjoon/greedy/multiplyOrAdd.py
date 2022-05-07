n = list(input())
print(n)
result = 0

for i in range(len(n)):
    if n[i] == 'j':
        continue
    print(i)
    if int(n[i]) == 0 or 1 and i != len(n)-1:
        result = int(n[i]) + int(n[i+1])
        n[i+1] = 'j'
            
    else:
        print('sibval')
        result *= int(n[i])
    print(result)

print(result)
