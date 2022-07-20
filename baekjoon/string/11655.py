arr = list(input())
ans = ""
for val in arr:
    if val.isalpha():
        a = ord(val)
        a += 13

        if a > 122 and val.islower():
            a -= 26
        elif a > 90 and val.isupper():
            a -= 26
        ans += chr(a)
    else:
        ans += val
print(ans)