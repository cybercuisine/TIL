MOD = 10007

N = int(input())
T = list(input())

dp = [[0] * 9 for _ in range(N + 1)]
dp[0][1] = 1

for i in range(N):
    sekinin = 0
    if T[i] == 'J':
        sekinin = 0
    elif T[i] == 'O':
        sekinin = 1
    else:
        sekinin = 2
    for bit in range(8):
        for bit2 in range(8):
            if not bit2 & (1 << sekinin):
                continue
            if not bit & bit2:
                continue
            dp[i + 1][bit2] += dp[i][bit]
            dp[i + 1][bit2] %= MOD

ans = 0
for i in range(8):
    ans += dp[N][i]
    ans %= MOD
print(ans)