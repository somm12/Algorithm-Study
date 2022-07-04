def isPrime(x):
    if x == 1:
        return False
    else:
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        else:
            return True

if __name__ == "__main__":

    ch = [0] * 246913
    
    for i in range(2, 246913):
        if isPrime(i):
            ch[i] = 1
  
    while True:
        n = int(input())
        count = 0
        if n == 0:
            break
        else:
            for k in range(n + 1, (2 * n) + 1):
                if ch[k] == 1:
                    count += 1
            print(count)
