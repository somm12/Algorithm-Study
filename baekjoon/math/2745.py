N, B = input().split()
B = int(B)
ans = 0
for i in range(len(N)):
    if not N[i].isdigit():
        ans += (ord(N[i]) - 55) * (B ** (len(N) - 1 - i))

    else:
        ans += int(N[i]) * (B ** (len(N) - 1 - i))
print(ans)