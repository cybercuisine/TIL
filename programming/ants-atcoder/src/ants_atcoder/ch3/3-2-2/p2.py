N, M = map(int, input().split())
f = [int(input()) for _ in range(N)]

MOD = 10**9 + 7

dp = [0] * (N + 1)
dp[0] = 1

using = [False] * (M + 1)
right = 0
left = 0
cum_sum = dp[0]
for r in range(N):
    while using[f[right]]:
        using[f[left]] = False
        cum_sum -= dp[left]
        cum_sum %= MOD
        left += 1

    dp[right + 1] = cum_sum
    cum_sum += dp[right + 1]
    cum_sum %= MOD
    using[f[right]] = True
    right += 1
print(dp[N])
