N = int(input())
X, Y = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]

dp = [[[float('inf')] * 301 for _ in range(301)] for _ in range(N + 1)]
dp[0][0][0] = 0

for i in range(N):
    A, B = AB[i]
    for j in range(301):
        for k in range(301):
            jj = min(j + A, 300)
            kk = min(k + B, 300)
            dp[i + 1][j][k] = min(dp[i + 1][j][k], dp[i][j][k])
            dp[i + 1][jj][kk] = min(dp[i + 1][jj][kk], dp[i][j][k] + 1)

ans = float('inf')
for i in range(X, 301):
    for j in range(Y, 301):
        ans = min(ans, dp[-1][i][j])

if ans == float('inf'):
    print(-1)
else:
    print(ans)