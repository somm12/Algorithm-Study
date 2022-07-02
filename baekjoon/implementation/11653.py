n = int(input())

    
if n != 1:
    temp = n
    while temp > 1:
        for i in range(2,n+1):
            if temp % i == 0:
                print(i)
                temp = temp // i
                break
            else:
                continue
