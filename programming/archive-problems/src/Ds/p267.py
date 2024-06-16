N, M = map(int, input().split())
A = list(map(int, input().split()))

dp = [[-float('inf')] * (M + 1) for _ in range(N + 1)]
dp[0][0] = 0

for i in range(1, N + 1):
    for j in range(M + 1):
        dp[i][j] = max(dp[i][j], dp[i-1][j])
        if j > 0:
            dp[i][j] = max(dp[i][j], dp[i-1][j-1] + j * A[i-1])

print(dp[N][M])
