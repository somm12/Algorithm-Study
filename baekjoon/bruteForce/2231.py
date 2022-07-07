def cal(x):
    sum = x
    while x > 0:
        sum += x % 10
        x = x // 10
    return sum

if __name__ == "__main__":
    n = int(input())
    temp = n
    ans = 0
    while True:
        temp -= 1
        res = cal(temp)
        if res == n:
            ans = temp
        elif temp < n // 2:
            break
    print(ans)
