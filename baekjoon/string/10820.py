
import sys
while True:
    arr = sys.stdin.readline().rstrip('\n')
    if not arr:
        break
    lowerCase = 0
    upperCase = 0
    number = 0
    space = 0
    for val in arr:
        if val.islower():
            lowerCase += 1
        elif val.isupper():
            upperCase += 1
        elif val.isdecimal():
            number += 1
        elif val.isspace():
            space += 1
    print(lowerCase, upperCase,number,space)
    


