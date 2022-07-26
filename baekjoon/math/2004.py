N, M = map(int, input().split())

def count_number(n, k):
    count = 0
    while n:
        n //= k
        count += n
    return count


five_count = count_number(N, 5) - count_number(M, 5) - count_number(N - M, 5)
two_count = count_number(N, 2) - count_number(M, 2) - count_number(N - M, 2)

answer = min(five_count, two_count)
print(answer)

# 팩토리얼로 구하면 시간초과 발생 
# 끝자리가 0이라는 것은 10의 배수
# 10은 2와 5로 구성되어 있음
# 2와 5 짝이 맞아야 10이 되므로 2의 개수와 5의 개수중 더 작은게 10의 개수이다.

# nCm = n! // ((n - m)! * m! ) 이기 때문에 n!에서의 5의 개수에서 m!과 (n - m)! 에서의 5의 개수를 
# 빼면 된다.