import sys
input = sys.stdin.readline

n = int(input())
arr = []
ch = [False] * n
ans = 100000000

def dfs(L, index):
    global ans
    if L == n // 2:
        star = 0
        link = 0
        for i in range(n):
            for j in range(i + 1, n):
                if ch[i] and ch[j]:
                    star += arr[i][j] + arr[j][i]
                elif not ch[i] and not ch[j]:
                    link += arr[i][j] + arr[j][i]
        ans = min(ans, abs(star - link))
    else:
        for i in range(index, n):
            if L == 0 or (not ch[i] and ch[0]):
                ch[i] = True
                dfs(L + 1, i + 1)
                ch[i] = False

for _ in range(n):
    arr.append(list(map(int,input().split())))

dfs(0,0)
print(ans)
# 느낀점. 
# 시간복잡도를 미리 생각하자. 
# 이전 풀이법 시간초과 난 이유: 조합은 O(2^n) => 20이면 100만, for중복 두번 -> 200번 + 조건문 다수 =>초과.
# 2차원 배열에서 숫자 맞추려고 index가 0 인 부분에 0을 insert 하지말자.
#  -> index out of range 오류 발생 막기 위함.
# 최소한의 반복문과 조건, 배열을 사용하자.