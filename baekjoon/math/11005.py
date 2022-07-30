n, B = map(int,input().split())
ans = ""

while n > 0:
    if n % B >= 10:
        ans = chr(55 + (n % B)) + ans
    else:
        ans = str(n % B) + ans
    n = n // B
print(ans)