max = 101
d = [[0] * 10 for _ in range(max)]

n = int(input())
d[1] = [0,1,1,1,1,1,1,1,1,1]
a = 1000000000

for i in range(2, max):
    for j in range(10):
        if j != 0 and j != 9:
            d[i][j] = d[i - 1][j + 1] + d[i - 1][j - 1]
        else:
            if j == 0:# 0으로 끝나는 자리 수 일때
                d[i][j] = d[i - 1][j + 1]
            else:# 9로 끝나는 자리 수 일 때
                d[i][j] = d[i - 1][j - 1]
        d[i][j] %= a
print(sum(d[n]) % a)