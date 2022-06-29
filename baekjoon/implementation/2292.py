sum = 1
count = 0
n = int(input())
while True:
    sum += count * 6
    if n <= sum:
        print(count + 1)
        break
    count += 1