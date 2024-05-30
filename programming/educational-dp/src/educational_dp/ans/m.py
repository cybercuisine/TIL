MOD = 10 ** 9 + 7

N, K = map(int, input().split())
a = list(map(int, input().split()))

dp = [[0] * (K + 1) for _ in range(N + 1)]
dp_sum = []
dp[0][0] = 1

for i in range(N):
    dp_sum.clear()
    dp_sum = [0] * (K + 2)
    for j in range(K + 1):
        dp_sum[j + 1] = (dp_sum[j] + dp[i][j]) % MOD
    for j in range(K + 1):
        dp[i + 1][j] = (dp_sum[j + 1] - dp_sum[j - min(j, a[i])]) % MOD

print(dp[N][K])