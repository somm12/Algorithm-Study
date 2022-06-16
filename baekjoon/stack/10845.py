from collections import deque
import sys
n = int(sys.stdin.readline())
q = deque()
for i in range(n):
    command = sys.stdin.readline().split()
    if len(command) == 2:
        q.append(int(command[1]))
 
    else:
        if command[0] == 'front':
            if q:
                print(q[0])
            else:
                print(-1)
        elif command[0] == 'back':
            if q:
                print(q[-1])
            else:
                print(-1)
        elif command[0] == 'size':
            print(len(q))
        elif command[0] == 'empty':
            if q:
                print(0)
            else:
                print(1)
        elif command[0] == 'pop':
            if q:
                x = q.popleft()
                print(x)
                
            else:
               print(-1)
