num1,num2 = input().split()
num1 = list(num1)
num2 = list(num2)

num1.reverse()
num2.reverse()

num1 = ''.join(num1)
num2 = ''.join(num2)

num1 = int(num1)
num2 = int(num2)

if num1 < num2:
    print(num2)
else:
    print(num1)