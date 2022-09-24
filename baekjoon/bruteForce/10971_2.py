
n = int(input())

arr = [ list(map(int,input().split())) for _ in range(n)]
minV = 100000000
visited = []
def dfs(result, start, end, visited):
    global minV
    if minV < result:
        return

    if len(visited) == n and arr[end][start] != 0:
        minV = min(minV, result + arr[end][start])
    else:
        for i in range(n):##
            if arr[end][i] != 0 and i not in visited:
                visited.append(i)
                dfs(result + arr[end][i], start, i, visited)##
                visited.pop()

for i in range(n):
    dfs(0, i, i,[i])###

print(minV)