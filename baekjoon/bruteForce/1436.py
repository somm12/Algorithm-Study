n = int(input())
res = [0]
count = 0
for i in range(666, 9666999):
    target  = str(i)
    if '666' in target:
        count += 1
        res.append(i)
        if count == n:
            break
print(res[n])