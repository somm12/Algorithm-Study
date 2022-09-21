ducks = input()
leng = len(ducks)

if leng % 5 != 0:
    print(-1)
    exit()

quack = "quack"
count = 0
visited = [0] * leng

def solve(s):
    global count 
    idx = 0
    keep = True
    for i in range(s, leng):
        if quack[idx] == ducks[i] and visited[i] == 0:
            visited[i] = 1
            if quack[idx] == 'k':
                idx = 0
                if keep:
                    count += 1
                    keep = False
            else:
                idx += 1
                continue


for i in range(leng):
    solve(i)

if count == 0 or all(visited) == False:
    print(-1)
else:
    print(count)