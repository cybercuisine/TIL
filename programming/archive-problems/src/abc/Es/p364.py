def MI():
    return map(int, input().split())


N, X, Y = MI()
AB = [list(MI()) for i in range(N)]

dp = [[[float('inf')] * (N + 1) for i in range(Y + 1)] for j in range(N + 1)]
dp[0][0][0] = 0

for i in range(1, N + 1):
    A, B = AB[i - 1]
    for j in range(Y + 1):
        for k in range(i + 1):
            dp[i][j][k] = dp[i - 1][j][k]
            if j - B >= 0 and k - 1 >= 0:
                dp[i][j][k] = min(dp[i][j][k], dp[i - 1][j - B][k - 1] + A)

ans = 0
for j in range(Y + 1):
    for k in range(N):
        if dp[N][j][k] <= X:
            ans = max(ans, k + 1)

print(ans)