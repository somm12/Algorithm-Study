max = 101
d = [[0] * 10 for _ in range(max)]

n = int(input())
d[1] = [0,1,1,1,1,1,1,1,1,1]
a = 1000000000

# d[i][j]는 i자리수에서 j라는 수로 끝나는 수의 개수를 의미.
# 끝자리가 0과 9일 때는 자리수 차이가 1이 가능한 것이 0은 앞자리가 1일때, 9는 앞자리가 8일때만 가능해서
# if 문으로 경우를 따로 나눈다.
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