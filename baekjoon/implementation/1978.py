def isPrime(x):
    if x == 1:
        return False

    for i in range(2, x//2 + 1):
        if x % i == 0:
            return False
    else:
        return True 

if __name__ == "__main__":
    n = int(input())
    count = 0
    arr = list(map(int,input().split()))
    
    for val in arr:
        res = isPrime(val)
        if res == True:
            count += 1
    print(count)
# 입력 받은 숫자를 2로 나눈 수는 입력 받은 수의 제일 큰 약수를 최소한으로 포함하는 범위가 된다.
# 이를 생각하면 x// 2 +1 까지만 확인해도 된다.
# 만약 15가 입력이면 15//2 + 1 => 7까지 확인. 실제로는 5가 가장 큰 약수이지만 적어도 제일 큰 약수
# 를 포함하는 최소한의 범위를 구하는 것이다.