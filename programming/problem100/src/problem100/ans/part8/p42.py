N, M = map(int, input().split())
dist = [int(input()) for _ in range(N)]
weather = [int(input()) for _ in range(M)]

INF = 10 ** 10
# 都市 i に j 日目にいるときの疲労度
dp = [[INF] * (M + 1) for _ in range(N + 1)]
dp[0] = [0] * (M + 1)

for i in range(N):
    for j in range(M):
        dp[i + 1][j + 1] = min(dp[i + 1][j], dp[i][j] + dist[i] * weather[j])


print(min(dp[N]))