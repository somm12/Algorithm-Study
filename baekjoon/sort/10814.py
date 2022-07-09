import sys
input = sys.stdin.readline

n = int(input())
arr = []

for i in range(n):
    age, name = input().split()
    age = int(age)
    arr.append((age,i,name))
arr.sort()

for age, num, name in arr:
    print(age, name)