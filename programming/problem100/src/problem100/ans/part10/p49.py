V, E = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(E)]

dist = [[float('inf')] * (V) for _ in range(V)]
for u in range(E):
    s, t, d = edges[u]
    dist[s][t] = d

dp = [[float('inf')] * (V) for _ in range(2 ** V)]
dp[0][0] = 0
for S in range(2 ** V):
    for v in range(V):
        for u in range(V):
            if not (S >> u) & 1 and S != 0:
                continue
            if (S >> v) & 1 == 0:
                if dp[S][u] + dist[u][v] < dp[S | (1 << v)][v]:
                    dp[S | (1 << v)][v] = dp[S][u] + dist[u][v]

if dp[2**V-1][0] != float('inf'):
    print(dp[2**V-1][0])
else:
    print(-1)