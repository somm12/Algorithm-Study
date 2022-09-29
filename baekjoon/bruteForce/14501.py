import sys
input = sys.stdin.readline

n = int(input())
p = []
t = []
ans = -1

def quit(day, total):
    global ans
    
    if day > n:
        return
    if day == n:
        ans = max(ans, total)
    else:
        quit(day + t[day], total + p[day])
        quit(day + 1, total)
for _ in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)
quit(0,0)
print(ans)
