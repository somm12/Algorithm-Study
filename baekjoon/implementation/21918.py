import sys
input = sys.stdin.readline
n , m = map(int ,input().split())
arr = list(map(int ,input().split()))

for _ in range(m):
    a, b, c= map(int ,input().split())
    if a== 1:
        arr[b - 1] = c
    elif a == 2:
        for i in range(b-1 , c):
            if arr[i] == 1:
                arr[i] = 0
            else:
                arr[i] = 1
    elif a == 3:
        # for문 대체로 인덱싱을 사용하여 0을 할당.
        arr[b-1:c] = [0] * (c-b+1)
    else:
        arr[b-1:c] = [1] * (c-b+1)

# for문 쓰지 않고 배열 내 원소를 띄어쓰기해서 출력.
print(*arr)
