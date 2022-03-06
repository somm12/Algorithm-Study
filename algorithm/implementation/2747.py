#fibonaci -> time limitation is short. That's why I did not use recursive part.
arr = [0 for i in range(46)]

def fibo(n):
    if n <= 1: 
        return n
    else:
        for i in range(n+1):
            if i <= 1:
                arr[i] = i
            else:
                arr[i] = arr[i-1] + arr[i-2]
        return arr[i]

n = int(input())
result = fibo(n)
print(result)