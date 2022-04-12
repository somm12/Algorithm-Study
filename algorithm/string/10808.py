string = input()
alphabet = [0 for i in range(26)]

for i in string:
    index = ord(i) - 97
    alphabet[index] +=1

for i in alphabet:
    print(i,end=' ')