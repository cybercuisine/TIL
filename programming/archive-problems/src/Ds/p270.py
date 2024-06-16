import sys
sys.setrecursionlimit(10**9)

N, K = map(int, input().split())
A = list(map(int, input().split()))

dp = [None] * (N + 1)

def dfs(now):
  if dp[now] != None:
    return dp[now]
  ret = 0
  for i in range(K):
    if A[i] <= now:
      ret = max(ret, A[i] + now - A[i] - dfs(now - A[i]))
  dp[now] = ret
  return ret

dfs(N)
print(dp[N])
