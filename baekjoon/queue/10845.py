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

# 출력해야하는 명령어가 주어질 때마다, 한 줄씩 출력해야한다는 문제를 제대로 읽지 않아서
# push 할 때도 출력이 되게끔 했더니.. 시간을 지체하며 틀렸다! 문제 잘 읽자.