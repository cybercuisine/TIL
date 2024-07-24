N = int(input())
S = list(input())

MOD = 10**9 + 7
T = "atcoder"

dp = [[0] * (len(T) + 1) for _ in range(N + 1)]
dp[0][0] = 1

for i in range(N):
    for j in range(len(T) + 1):
        dp[i + 1][j] += dp[i][j]
        dp[i + 1][j] %= MOD

        if j < len(T) and S[i] == T[j]:
            dp[i + 1][j + 1] = dp[i][j]
            dp[i + 1][j + 1] %= MOD

print(dp[N][len(T)])