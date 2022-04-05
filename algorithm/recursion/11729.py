n = int(input())
a = []
def Hanoi(From,by,to,n):
    if n == 1:
        a.append(str(From)+' '+str(to))
    else:    
        Hanoi(From,to,by,n-1)
        a.append(str(From)+' '+str(to))
        Hanoi(by,From,to,n-1)

Hanoi(1,2,3,n)
print(len(a))
for i in a:
    print(i)