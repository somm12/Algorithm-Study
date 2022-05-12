import statistics
import sys
from typing import Counter
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for x in range(n)]
arr.sort()
#산술평균
print(round(sum(arr)/len(arr)))
#중앙값
print(arr[(len(arr)//2)])
#최빈값
if len(arr) == 1:
    print(arr[0])
else:
    li = Counter(arr)
    mostCountedValue1 = statistics.mode(arr)
    newArr = [i for i in arr if i is not mostCountedValue1]
    mostCountedValue2 = statistics.mode(newArr)


    if li[mostCountedValue1] == li[mostCountedValue2]:
        print(max(mostCountedValue1,mostCountedValue2))
    else:
        print(mostCountedValue1)

#범위
if len(arr) <= 1:
    print(0)
else:
    print(arr[-1]-arr[0])
