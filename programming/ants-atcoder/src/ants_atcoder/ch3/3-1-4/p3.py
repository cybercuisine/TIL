N, A = map(int, input().split())
X = list(map(int, input().split()))

dp = [[0] * (N * 50 + 1) for _ in range(N + 1)]

dp[0][0] = 1

for i in range(1, N + 1):
    xi = X[i - 1]
    for k in range(N, 0, -1):
        for s in range(N * 50, xi - 1, -1):
            dp[k][s] += dp[k - 1][s - xi]

ans = 0
for k in range(1, N + 1):
    ans += dp[k][A * k]

print(ans)
