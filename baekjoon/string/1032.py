n = int(input())
dir = []
result = ""
count = 0
for i in range(n):
    dir.append(input())
for i in range(1,n):
    for k in range(len(dir[0])):
        if dir[0][k] == dir[i][k]:
            result += dir[0][k]
        else:
            result += "?" 
    dir[0] = result
    result = ""
print(dir[0])