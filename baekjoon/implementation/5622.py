from operator import index
from unittest import result


alphabet = [3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,8,9,9,9,10,10,10,10]

string = list(input())
result = 0
for i in range(len(string)):
    index= ord(string[i]) - 65
    result += alphabet[index]
print(result)

