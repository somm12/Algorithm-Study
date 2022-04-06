
import sys
n = int(sys.stdin.readline())
a = []
def Hanoi(From,by,to,n):
    if n == 1:
        a.append(str(From)+' '+str(to))
    else:    
        Hanoi(From,to,by,n-1)
        a.append(str(From)+' '+str(to))
        Hanoi(by,From,to,n-1)


print((1 << n) - 1)
if n <=20:
    Hanoi(1,2,3,n)
    for i in a:
        print(i)

   
    
