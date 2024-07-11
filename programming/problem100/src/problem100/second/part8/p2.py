N, W = map(int, input().split())
VW = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * (W + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    v, w = VW[i - 1]
    for j in range(W + 1):
        dp[i][j] = dp[i - 1][j]
        if j - w >= 0:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)

print(max(dp[-1]))