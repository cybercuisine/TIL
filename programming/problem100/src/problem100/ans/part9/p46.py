N = int(input())
matrices = [tuple(map(int, input().split())) for _ in range(N)]

p = [matrices[0][0]] + [matrices[i][1] for i in range(N)]

dp = [[0] * N for _ in range(N)]

for length in range(2, N + 1):
    for i in range(N - length + 1):
        j = i + length - 1
        dp[i][j] = float('inf')
        for k in range(i, j):
            q = dp[i][k] + dp[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
            if q < dp[i][j]:
                dp[i][j] = q

print(dp[0][N - 1])
