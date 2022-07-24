array = [True for i in range(1000001)]
#에라토스테네스 체
for i in range(2, 1001):
    if array[i]:
        for k in range(i + i, 1000001, i):
            array[k] = False

while True:
    n = int(input())
    if n == 0:
        break

    for i in range(3, len(array)):
        if array[i] and array[n - i]:
            print("%d = %d + %d" %(n, i, n - i))
            break