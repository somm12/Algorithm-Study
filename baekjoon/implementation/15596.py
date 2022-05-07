import sys
sys.setrecursionlimit(10**7)

def solve(a: list):
	result = 0
	for i in range(len(a)):
		result += a[i]
	return result
