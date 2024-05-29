N, W = map(int, input().split())
wv = [tuple(map(int, input().split())) for _ in range(N)]

dp = [[0] * (W + 1) for _ in range(N + 1)]

for i in range(N):
    w, v = wv[i]
    for j in range(W + 1):
        if j - w >= 0:
            dp[i+1][j] = max(dp[i][j-w] + v, dp[i][j])
        else:
            dp[i+1][j] = dp[i][j]

ans = 0
for s in dp:
    for t in s:
        ans = max(ans, t)

print(ans)