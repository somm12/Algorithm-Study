string = input()
string = string.lower()
alpha = list(set(string))
alpha_count = []

for value in alpha:
    if value in string:
        result = string.count(value)
        alpha_count.append(result)

N = max(alpha_count)

if alpha_count.count(N) > 1:
    print("?")
else:
    index = alpha_count.index(N)
    print(alpha[index].upper())

