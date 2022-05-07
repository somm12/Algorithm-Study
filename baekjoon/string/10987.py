from itertools import count


word = input()
count = 0
for alphabet in word:
    if alphabet == 'a' or alphabet == 'e' or alphabet == 'i' or alphabet =='o'or alphabet=='u':
        count +=1
print(count)
