
def isPrime(x):
    if x == 1:
        return False
    else:
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        else:
            return True

if __name__ == "__main__":
    m, n = map(int,input().split())
    for i in range(m, n + 1):
        if isPrime(i):
            print(i)