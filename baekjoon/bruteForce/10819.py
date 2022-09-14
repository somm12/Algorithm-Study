def dfs(L):
  global ans
  if L == n:
    s = 0
    for i in range(0, n - 1):
      s += abs(res[i] - res[i + 1])
    ans = max(ans, s)
  else:
    for i in range(n):
      if check[i] == 0:
        check[i] = 1
        res[L] = arr[i]
        dfs(L + 1)
        check[i] = 0

if __name__ == "__main__":
  n = int(input())
  arr = list(map(int,input().split()))
  check = [0] * n
  res = [0] * n
  ans = -1
  dfs(0)
  print(ans)