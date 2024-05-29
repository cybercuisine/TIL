N, M = map(int, input().split())
path = [tuple(map(int, input().split())) for _ in range(M)]

dist = [[float('inf')] * N for _ in range(N)]
times = [[0] * N for _ in range(N)]
for s, t, d, time in path:
    dist[s-1][t-1] = d
    times[s-1][t-1] = time
    dist[t-1][s-1] = d
    times[t-1][s-1] = time


dp = [[[float('inf'), 0]] * N for _ in range(2 ** N)]
dp[0][0] = [0, 1]

for i in range(2 ** N):
    for j in range(N):
        if (i >> j) & 1 == 0:
            for k in range(N):
                if dp[i][k][0] + dist[k][j] <= times[k][j]:
                    if dp[i][k][0] + dist[k][j] == dp[i+2**j][j][0]:
                        dp[i + 2**j][j][1] += dp[i][k][1]
                    elif dp[i][k][0] + dist[k][j] < dp[i + 2**j][j][0]:
                        dp[i + 2**j][j] = [dp[i][k][0] + dist[k][j], dp[i][k][1]]

if dp[2**N-1][0][0] == float('inf'):
    print('IMPOSSIBLE')
else:
    print(*dp[2**N-1][0])