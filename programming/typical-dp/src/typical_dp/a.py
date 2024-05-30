N = int(input())
P = list(map(int, input().split()))
M = 100


dp = [[0] * (N * M + 1) for _ in range(N + 1)]
dp[0][0] = 1

for i, a in enumerate(P):
    for j in range(N * M + 1):
        dp[i + 1][j] = dp[i][j]
        if j >= a:
            dp[i + 1][j] |= dp[i][j - a]

print(sum(dp[N]))