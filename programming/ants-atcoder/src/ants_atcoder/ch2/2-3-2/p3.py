N, M = map(int, input().split())
C = [list(map(int, input().split())) for _ in range(N)]
P = [list(map(int, input().split())) for _ in range(M)]

dp = [[[0] * 102 for _ in range(102)] for _ in range(102)]

for a, b, c, w in C:
    dp[a][b][c] = max(dp[a][b][c], w)

for i in range(101):
    for j in range(101):
        for k in range(101):
            dp[i + 1][j][k] = max(dp[i + 1][j][k], dp[i][j][k])
            dp[i][j + 1][k] = max(dp[i][j + 1][k], dp[i][j][k])
            dp[i][j][k + 1] = max(dp[i][j][k + 1], dp[i][j][k])
            dp[i + 1][j + 1][k] = max(dp[i + 1][j + 1][k], dp[i][j + 1][k], dp[i + 1][j][k])
            dp[i + 1][j][k + 1] = max(dp[i + 1][j][k + 1], dp[i][j][k + 1], dp[i + 1][j][k])
            dp[i][j + 1][k + 1] = max(dp[i][j + 1][k + 1], dp[i][j][k + 1], dp[i][j + 1][k])
            dp[i + 1][j + 1][k + 1] = max(dp[i + 1][j + 1][k + 1], dp[i][j + 1][k + 1], dp[i + 1][j][k + 1], dp[i + 1][j + 1][k])

for x, y, z in P:
    print(dp[x][y][z])
