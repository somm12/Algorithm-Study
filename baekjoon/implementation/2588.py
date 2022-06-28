a = int(input())
b = int(input())
result = a * b
while b > 0:
    digit = b % 10
    b = b // 10
    print(a * digit)
print(result)