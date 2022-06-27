

def dfs(x,y,count,res):
    res += g[x][y]
    if count == 6:
        answer.add(res)
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
            continue
        dfs(nx,ny,count+1,res)

if __name__ == "__main__":
    g = []
    answer = set()
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    for _ in range(5):
        g.append(list(input().split()))
    for x in range(5):
        for y in range(5):
            count = 0
            res = ''
            dfs(x,y,count+1,res)
    print(len(answer))

