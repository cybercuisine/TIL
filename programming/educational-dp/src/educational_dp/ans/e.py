N, W = map(int, input().split())
WV = [tuple(map(int, input().split())) for _ in range(N)]

max_value = sum(v for _, v in WV)
dp = [[float('inf')] * (max_value + 1) for _ in range(N + 1)]
dp[0][0] = 0

for i in range(N):
    w, v = WV[i]
    for j in range((max_value + 1)):
        if j - v >= 0:
            dp[i + 1][j] = min(dp[i][j - v] + w, dp[i][j])
        else:
            dp[i + 1][j] = dp[i][j]

ans = 0
for i in range((max_value + 1)):
    if dp[N][i] <= W:
        ans = i

print(ans)