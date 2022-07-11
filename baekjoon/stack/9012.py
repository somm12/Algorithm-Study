import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    arr = ""
    stack = []
    arr = input().rstrip()
   
    for i in arr:
        if not stack:
            stack.append(i)
        else:
            if stack[-1] != i:
                if stack[-1] == ")":
                    stack.append(i)
                else: stack.pop()
            else:
                stack.append(i)
    
    if stack:
        print("NO")
    else:
        print("YES")

# 올바른 괄호는 여괄호가 닫는 괄호와 쌍을 이루어 만났을 때일 뿐이다.
# )( 와 같은 예시는 올바를 괄호가 아님.