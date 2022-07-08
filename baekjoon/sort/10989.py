import sys
input = sys.stdin.readline

if __name__ == "__main__":
    ch = [0] * 10001
    n = int(input())

    for _ in range(n):
       a = int(input())
       ch[a] += 1
    for i in range(len(ch)):
        if ch[i] > 0 :
            for _ in range(ch[i]):
                print(i)
# counting sort: 계수 정렬