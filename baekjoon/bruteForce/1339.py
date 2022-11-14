from itertools import permutations


n = int(input())
a = []
k = set()
maxV = -1e9

def sol(arr):
    result = dict([])
    # 딕셔너리 만들기 : {'A': 1 ,,,}
    for i in range(len(arr)):
        result[k[i]] = arr[i]
    ans = []
    for v in a:
        s = ''# '123' '12345' 매칭된 숫자들을 문자열로 변환
        for c in v:
            s += str(result[c])
        ans.append(s)
    A = 0
    for v in ans:
        A += int(v)
    return A


for _ in range(n):
    a.append(input())
for v in a:
    for c in v:
        k.add(c)
k = list(k)
for d in set(permutations([i for i in range(10)], len(k))):
    maxV = max(maxV, sol(d))
print(maxV)

## 위의 코드는 메모리 초과. permutation 사용은 메모리를 많이 차지. 순열을 쓰지않고 그리디로 풀이가능.

