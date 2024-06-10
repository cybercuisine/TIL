N, M, L, X = map(int, input().split())
A = list(map(int, input().split()))

dp = [[float('inf')] * (M) for _ in range(N + 1)]
dp[0][0] = 1

for i in range(N):
    a = A[i]
    for j in range(M):
        dp[i + 1][(j + a) % M] = min(dp[i][(j + a) % M], dp[i][j] + (j + a) // M)

if dp[N][L] <= X:
    print("Yes")
else:
    print("No")