from itertools import combinations
import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
visited = [0] * ((10**6)*2 + 1)
for i in range(1, n + 1):
    for v in list(combinations(arr, i)):
        visited[sum(v)] = 1

for i in range(1, len(visited)):
    if visited[i] == 0:
        print(i)
        break