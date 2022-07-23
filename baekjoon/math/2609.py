a, b = map(int,input().split())
ans1 = 1
ans2 = 1
arr1 = []
arr2 = []

for i in range(1, a + 1):
    if a % i == 0:
        arr1.append(i)
arr1.reverse()

for i in range(1, b + 1):
    if b % i == 0:
        arr2.append(i)
for val in arr1:
    if val in arr2:
        ans1 = val
        break

ans2 = ans1 * (a//ans1) * (b//ans1)
print(ans1)
print(ans2)