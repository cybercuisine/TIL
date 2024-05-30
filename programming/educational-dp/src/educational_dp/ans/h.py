MOD = 10 ** 9 + 7

H, W = map(int, input().split())
A = [input() for _ in range(H)]

dp = [[0] * (W) for _ in range(H)]
dp[0][0] = 1

for i in range(H):
    for j in range(W):
        if A[i][j] == '#':
            continue
        if i > 0:
            dp[i][j] += dp[i-1][j]
        if j > 0:
            dp[i][j] += dp[i][j-1]
        dp[i][j] %= MOD

print(dp[H-1][W-1])