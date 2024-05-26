N, W = map(int, input().split())
values = [tuple(map(int, input().split())) for _ in range(N)]

dp = [[0] * (W + 1) for _ in range(N + 1)]

for i in range(N):
    value = values[i][0]
    weight = values[i][1]
    for j in range(W + 1):
        if j >= weight:
            dp[i + 1][j] = max(dp[i][j - weight] + value, dp[i][j])
        else:
            dp[i + 1][j] = dp[i][j]

print(dp[N][W])