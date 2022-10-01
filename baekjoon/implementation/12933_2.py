s = input()
size = len(s)
visited = [0] * size
quack = 'quack'
count = 0

if size % 5 != 0:
    print(-1)
    exit()
def sol(start):
    global count
    idx = 0
    keep = True
    for i in range(start, size):
        if s[i] == quack[idx] and visited[i] == 0:
            visited[i] = 1
            if quack[idx] == 'k':
                if keep:
                    count += 1
                    keep = False
                idx = 0
            else:
                idx += 1

for i in range(size):
    sol(i)

if count == 0 or not all(visited):
    print(-1)
else:
    print(count)