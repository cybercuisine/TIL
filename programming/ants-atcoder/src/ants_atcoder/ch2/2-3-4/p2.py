N, K = map(int, input().split())
A = [int(input()) for _ in range(N)]


INF = 10 ** 18
dp = [INF] * (N + 1)
dp[0] = 0
cnt = 0

for i in range(N):
  a = A[i]
  if i == 0:
    dp[1] = 1
  else:
    for j in range(N, 0, -1):
      num = dp[j - 1] * (cnt + a) // cnt + 1
      if num - dp[j - 1] <= a:
        dp[j] = min(dp[j], num)
  cnt += a

if cnt == K:
  print(1)
  exit()

for i in range(N, - 1, -1):
  if dp[i] <= K:
    print(i)
    exit()