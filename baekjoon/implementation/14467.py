n = int(input())
cnt = 0
arr = [0] * 11
ch = [0] * 11

for _ in range(n):
    i, j = map(int, input().split())
    if arr[i] != j and ch[i] == 1:
        cnt += 1
        arr[i] = j
    else:
        ch[i] = 1
        arr[i] = j
print(cnt)