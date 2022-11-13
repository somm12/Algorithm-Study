n = int(input())
arr = list(map(int, input().split()))
ops = list(map(int, input().split()))
maxV, minV = -1e9, 1e9

def solve(index, ans, add, sub, mul, div) :
    global maxV, minV
    if index >= n :
        maxV = max(maxV, ans)
        minV = min(minV, ans)
        return
    if add > 0 :
        solve(index+1, ans+arr[index], add-1, sub, mul, div)
    if sub > 0 :
        solve(index+1, ans-arr[index], add, sub-1, mul, div)
    if mul > 0 :
        solve(index+1, ans*arr[index], add, sub, mul-1, div)
    if div > 0 :
        solve(index+1, ans//arr[index] if ans > 0 else -((-ans)//arr[index]), add, sub, mul, div-1)

solve(1, arr[0], ops[0], ops[1], ops[2], ops[3])
print(maxV)
print(minV)