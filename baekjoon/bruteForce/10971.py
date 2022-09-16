def dfs(start, next, total, visited):
    global minV
    if total > minV:
        return

    if len(visited) == n:
        if arr[next][start] != 0:
            minV = min(minV, total + arr[next][start])
    else:
        for i in range(n):
            if arr[next][i] != 0 and i not in visited:
                visited.append(i)
                dfs(start, i ,total + arr[next][i], visited)
                visited.pop()
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
minV = 10**7
for i in range(n):
    dfs(i,i,0,[i])       
print(minV)