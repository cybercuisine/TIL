N, S, K = map(int, input().split())
mod = 10 **9 + 7


S -= N *((N - 1) * K) // 2


def div_num(S, N):
    dp = (S + 1) * [1]
    for i in range(2, N + 1):
        for j in range(i, S + 1):
            dp[j] = (dp[j] + dp[j - i]) % mod
    return dp[-1]

if S < 0:
     print(0)
else:
    print(div_num(S, N))
