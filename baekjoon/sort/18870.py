import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

sortedArr = list(set(arr))
sortedArr.sort()
dic = {sortedArr[i] : i for i in range(len(sortedArr))}

for i in range(len(arr)): 
    print(dic[arr[i]],end=' ')
    #index메소드는 시간복잡도가 N이다. ->  시간초과발생
    #print(sortedArr.index(arr[i]),end=' ')