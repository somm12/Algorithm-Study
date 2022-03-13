N,M = map(int, input().split())
arr = []
#input with no space,, how?
for i in range(N):
    a = list(input())
    arr.append(a)

print()

for i in range(N):
    for k in range(M):
        print(arr[i][k], end='')
    print()