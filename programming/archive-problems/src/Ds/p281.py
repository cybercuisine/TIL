N, K, D = map(int, input().split())
A = list(map(int, input().split()))

dp = [[[-1] * D for _ in range(K + 1)] for _ in range(N + 1)]
dp[0][0][0] = 0

for i in range(1, N + 1):
    for j in range(K + 1):
        for k in range(D):
            if dp[i - 1][j][k] != -1:
                dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j][k])
            if j > 0 and dp[i - 1][j - 1][(k - A[i - 1]) % D] != -1:
                dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j - 1][(k - A[i - 1]) % D] + A[i - 1])


print(dp[N][K][0])
