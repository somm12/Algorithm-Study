import sys
sys.setrecursionlimit(10 ** 6)
dw = [0,0,-1,1,-1,1,-1,1]
dh = [-1,1,0,0,-1,-1,1,1]



def bfs(arr,h,w):
    arr[h][w] = -1 #방문처리
    for i in range(8):
        x = dw[i] + w
        y = dh[i] + h
        if x < 0 or y < 0 or x >=len(arr[0]) or y >=len(arr):
            continue
        if arr[y][x] == 1:
            bfs(arr,y,x)

while True:
    w,h = map(int, input().split())
    if w==0 and h == 0:
        break
    arr = []
    count = 0
    for i in range(h):
        arr.append(list(map(int,input().split())))
    
    for i in range (h):
        for k in range(w):
            if arr[i][k] == 1:
                bfs(arr,i,k)
                count += 1

    print(count)


