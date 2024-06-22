N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]
MOD = 998244353

dp = [[0] * 2 for i in range(N)]
dp[0][1] = 1
dp[0][0] = 1

for i in range(1, N):
    a0, b0 = AB[i - 1]
    a1, b1 = AB[i]

    ura = 0
    if a0 != b1:
        ura += dp[i - 1][0]
    if b0 != b1:
        ura += dp[i - 1][1]
    dp[i][1] += (ura % MOD)

    omote = 0
    if a0 != a1:
        omote += dp[i - 1][0]
    if b0 != a1:
        omote += dp[i - 1][1]
    dp[i][0] += (omote % MOD)

print(sum(dp[-1]) % MOD)