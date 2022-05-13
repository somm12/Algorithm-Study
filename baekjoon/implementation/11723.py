import sys
n = int(input())
S = set()
for i in range(n):
    command = sys.stdin.readline().strip()
    if command == "all":
        S.clear()
        S = set([j for j in range(1,21)])
    elif command == "empty":
        S.clear()
    
    else:
        command,element = command.split()
        element = int(element)
        if command == "add":
            S.add(element)
        elif command == "remove":
            S.discard(element)
        elif command == "check":
            if element in S:
                print(1)
            else:
                print(0)
        elif command == "toggle":
            if element in S:
                S.discard(element)
            else:
                S.add(element)
   
