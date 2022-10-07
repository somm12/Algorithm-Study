import sys
input = sys.stdin.readline().strip()
arr = input
n = len(arr)
quack = 'quack'
count = 0
visited = [0] * n
if n % 5 != 0:
    print(-1)
    exit()

def sol(start):
    global count
    keep = True
    idx = 0
    for i in range(start, n):
        if arr[i] == quack[idx] and visited[i] == 0:
            visited[i] = 1
            if quack[idx] == 'k':
                if keep:
                    count += 1
                    keep = False
                idx = 0
            else:
                idx += 1

for i in range(n):
    sol(i)
if count == 0 or not all(visited):
    print(-1)
else:
    print(count)
