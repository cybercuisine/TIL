N = int(input())
A = list(map(int, input().split()))

mod = 998244353

answer = 0
for l in range(1, N + 1):
    dp = [[[0 for k in range(l)] for j in range(l + 1)] for i in range(N + 1)]

    for i in range(N + 1):
        dp[i][0][0] = 1

    for i in range(1, N + 1):
        for j in range(1, l + 1):
            for k in range(l):
                dp[i][j][k] += dp[i - 1][j][k]

                dp[i][j][k] += dp[i - 1][j - 1][(k - (A[i - 1] % l)) % l]

                dp[i][j][k] %= mod

    answer += dp[N][l][0] % mod

print(answer % mod)
