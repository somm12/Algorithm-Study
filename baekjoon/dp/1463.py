n = int(input())

d = [0] * (n+1)
d[1] = 0


if n <= 1:
    print(d[n])
    exit(0)
else:
    for i in range(2, n + 1):
        a = 1000000
        b = 1000000
        c = 1000000
        if i % 2 == 0:
            a = d[i // 2] + 1
        if i % 3 == 0:
            b = d[i // 3] + 1       
        c = d[i - 1] + 1
        d[i] = min(a, b, c)
print(d[n])
