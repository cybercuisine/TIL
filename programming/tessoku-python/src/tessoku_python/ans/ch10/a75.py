N = int(input())
problems = [list(map(int, input().split())) for _ in range(N)]
problems.sort(key=lambda p: p[1])

MAX_D = max(map(lambda p: p[1], problems))
dp = [[-(10**10)] * (MAX_D + 1) for _ in range(N + 1)]
dp[0][0] = 0

for i in range(N):
    t, d = problems[i]
    for j in range(MAX_D + 1):
        if j > d or j < t:
            dp[i + 1][j] = dp[i][j]
        else:
            dp[i + 1][j] = max(dp[i][j], dp[i][j - t] + 1)

ans = max(dp[N])
print(ans)