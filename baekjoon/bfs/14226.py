from collections import deque


n = int(input())

def bfs():
    screen = deque([1])
    board = deque([0])
    count = deque([0])
    while True:
        s = screen.popleft()
        b = board.popleft()
        c = count.popleft()
        if s == n:
            print(c)
            exit()
        screen.append(s)
        board.append(s)
        count.append(c + 1)

        screen.append(s + b)
        board.append(b)
        count.append(c + 1)

        screen.append(s-1)
        board.append(b)
        count.append(c + 1)
bfs()