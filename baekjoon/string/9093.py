import sys

n = int(input())
result = []
reversedSentence = []

for i in range(n):
    sentence = list(sys.stdin.readline().strip().split(" "))
    for word in sentence:
        reversedSentence.append(word[::-1])
    result.append(reversedSentence)
    reversedSentence = []

for sentence in result:
    for word in sentence:
        print(word,end=' ')
    print()
