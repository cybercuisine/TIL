
mod = 10 ** 4
N, K = map(int, input().split())

A = [0] * N

for k in range(K):
    a, b = map(int, input().split())
    A[a - 1] = b

dp = [[[0] * 4 for i in range(4)] for j in range(N + 1)]
dp[0][0][0] = 1

for n in range(N):
    for i in range(4):
        for j in range(4):
            for k in range(1, 4):
                if A[n] != 0 and A[n] != k:
                    continue
                if k != i or i != j:
                    dp[n + 1][k][i] += dp[n][i][j]
                    dp[n + 1][k][i] %= mod

ans = 0
for i in range(4):
    for j in range(4):
        ans += dp[-1][i][j]
        ans %= mod

print(ans)
                    