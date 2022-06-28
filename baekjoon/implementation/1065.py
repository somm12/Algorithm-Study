n = int(input())

if n < 100:
    ans = n
else:
    ans = 99
    for i in range(100, n + 1):
        # 각 자리수 숫자를 담는 배열 digit
        digit = []
        while i > 0:
            digit.append(i % 10)
            i = i // 10
        d = set()
        # 각 자리수의 차를 구해서 집합에 추가, 만약 하나라도 다른 차가 나온다면 한수에 해당X
        for k in range(len(digit) - 1):
            d.add(digit[k] - digit[k + 1])
        if len(d) == 1:
            ans += 1
print(ans)