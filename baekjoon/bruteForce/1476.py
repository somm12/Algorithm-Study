E, S, M = map(int,input().split())

for i in range(532):
    for j in range(532):
        for k in range(532):
            if E + 15*i == S + 28*j == M + 19*k:
                ans = E + 15*i
                break
print(ans)