def isPrime(x):
    if x == 1:
        return False
    for i in range(2, x//2 + 1):
        if x % i == 0:
            return False
    else:
        return True

if __name__ == "__main__":
    m = int(input())
    n = int(input())

    sum = 0
    min = 2147000000
    for i in range(m, n+1):
        if isPrime(i):
            sum += i
            if min > i:
                min = i
    if sum != 0:
        print(sum)
        print(min)
    else:
        print(-1)