string = input()
string = string.split(" ")
count = 0
for value in string:
    if value == "":
        count += 1

print(len(string)-count)