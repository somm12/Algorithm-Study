from collections import deque
n = int(input())
q = deque()
for i in range(n):
    command = input().split()
    if len(command) == 2:
        q.append(int(command[1]))
        print(command[1])
 
    else:
        if command[0] == 'front':
            if len(q) == 0:
                print(0)
            else:
                print(q[-1])
        elif command[0] == 'back':
            if len(q) == 0:
                print(-1)
            else:
                print(q[-1])
        elif command[0] == 'size':
            print(len(q))
        elif command[0] == 'empty':
            if len(q)== 0:
                print(1)
            else:
                print(0)
        elif command[0] == 'pop':
            if len(q) == 0:
                print(-1)
            else:
                x = q.popleft()
                print(x)
