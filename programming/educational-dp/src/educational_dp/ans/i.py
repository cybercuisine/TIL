N = int(input())
p = list(map(float, input().split()))

dp = [[0] * (N + 1) for _ in range(N + 1) ]
dp[0] = [0 if i else 1 for i in range(N + 1)]

for i in range(1, N + 1):
  for j in range(N + 1):
    if i < j:
      dp[i][j] = 0
    elif j == 0:
      dp[i][0] = dp[i - 1][0] * (1 - p[i - 1])
    else:
      dp[i][j] = dp[i - 1][j - 1] * p[i - 1] + dp[i - 1][j] * (1 - p[i - 1])
      
print(sum(dp[N][j] for j in range(N//2 + 1, N + 1)))