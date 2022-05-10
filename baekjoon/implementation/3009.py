
coordinateX = []
coordinateY = []
for i in range(3):
    x,y = map(int,input().split())
    coordinateX.append(x)
    coordinateY.append(y)

coordinateX.sort()
coordinateY.sort()

def countNumber(arr,number):
    count = 0
    for i in arr:
        if i == number:
            count += 1
    if count == 2:
        return arr[0]
    else:
        return arr[2]
X = countNumber(coordinateX,coordinateX[2])
Y = countNumber(coordinateY,coordinateY[2])
print(X,Y)

