N = int(input())
A = list(map(int, input().split()))

num1, num2, num3 = A.count(1), A.count(2), A.count(3)
dp = [[[-1] * (N + 1) for _ in range(N + 1)] for _ in range(N + 1)]
dp[0][0][0] = 0

for k in range(num3 + 1):
  for j in range(num2 + num3 - k + 1):
    for i in range(num1 + num2 + num3 - j - k + 1):
      if i == j == k == 0:
        continue
      tmp = N 
      if 0 < i:
        tmp += i * dp[i - 1][j][k]
      if 0 < j:
        tmp += j * dp[i + 1][j - 1][k]
      if 0 < k:
        tmp += k * dp[i][j + 1][k - 1]
      dp[i][j][k] = tmp / (i + j + k)

print(dp[num1][num2][num3])