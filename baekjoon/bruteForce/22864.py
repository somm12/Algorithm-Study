
a, b, c, m = map(int,input().split())
if a > m:
    print(0)
    exit()
day = 0
w = 0
p = 0

while day != 24:
    day += 1
    if p < 0:
        p = 0
    if p + a <= m:
        p += a
        w += b
    else:
        p -= c

print(w)

# 재귀로 풀면 깊이가 24로 깊어져서 시간 초과가 나기에, 반복문이 유리하다.