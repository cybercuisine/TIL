N, M = map(int, input().split())
A = [int(input()) - 1 for _ in range(N)]
S = [[0] * (N + 1) for _ in range(M)]
for m in range(M):
    for n in range(N):
        S[m][n + 1] = S[m][n] + (A[n] == m)

ALL = 1 << M
INF = 10 ** 18
dp = [INF] * ALL
dp[0] = 0

for bit in range(1, ALL):
    r = 0
    for m in range(M):
        if (bit >> m) & 1 == 1:
            r += S[m][N]
    for m in range(M):
        if (bit >> m) & 1 == 0:
            continue
        l = r - S[m][N]
        add = r - l - (S[m][r] - S[m][l])
        dp[bit] = min(dp[bit], dp[bit & ~(1 << m)] + add)

ans = dp[ALL - 1]
print(ans)