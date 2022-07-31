max = 0
N = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
arr = []

for _ in range(N):
    arr.append(list(input()))

def area():
    global max
    area = 1
    for i in range(N):
        for j in range(N - 1):
            if arr[i][j] == arr[i][j + 1]:
                area += 1
            if area > max:
                max = area
            if arr[i][j] != arr[i][j + 1]:
                area = 1
        
        area = 1
    
    for i in range(N):
        for j in range(N - 1):
            if arr[j][i] == arr[j + 1][i]:
                area += 1
            if area > max:
                max = area
            if arr[j][i] != arr[j + 1][i]:
                area = 1
        area = 1
for i in range(N):
    for j in range(N):
        for k in range(4):
            X = i + dx[k]
            Y = j + dy[k]
            if X < 0 or Y < 0 or X >= N or Y >= N:
                continue
            else:
                if arr[X][Y] != arr[i][j]:
                    arr[i][j], arr[X][Y] = arr[X][Y], arr[i][j]
                    area()
                    arr[i][j], arr[X][Y] = arr[X][Y], arr[i][j]
                else:
                    continue
print(max)