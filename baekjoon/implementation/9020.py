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
    
    ch = [0] * 10001
    partition1 = 0
    partition2 = 0
    for i in range(2, 10001):
        if isPrime(i):
            ch[i] = 1

    n = int(input())

    for _ in range(n):
        m = int(input())
        # 파티션이 여러개면 파티션1,2 차이가 적은 경우 출력. m이 10이면 5 + 5 경우가 차이가 0 이다. 
        # 따라서 m//2 값을 넘어서면 두 파티션의 차이가 더 증가하므로 m//2까지만 확인하고 마지막 파티션이
        # 차이가 가장 작은 경우가 된다.
        for k in range(2, (m // 2) + 1):
            if ch[k] == 1:
                if ch[m - k] == 1:
                    partition1 = k
                    partition2 = m - k
        print(partition1, partition2)

# 10000 이하의 짝수의 골드바흐 파티션 1,2를 구하자, 
# ex) 10 = 5 + 5, 3 + 7 와 같이 소수의 합으로 짝수를 만들 수 있고, 여러개 파티션이 있다면
# 해당 파티션 값들의 차이가 작은 경우를 찾아야한다.