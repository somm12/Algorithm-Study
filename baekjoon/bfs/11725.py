from collections import deque


n = int(input())
graph = [[] for _ in range(n + 1)]
# 답을 담은 배열 answer가 방문표시 배열 역할을 동시에 한다.
answer = [0] * (n + 1)

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
def bfs():
    q = deque([1])
    answer[1] = 1
    while q:
        x = q.popleft()    
        for i in graph[x]:
            if not answer[i]:
                answer[i] = x
                q.append(i)

bfs()
for i in range(2, n + 1):
    print(answer[i])                