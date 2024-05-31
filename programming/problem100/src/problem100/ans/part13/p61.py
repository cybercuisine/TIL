INF = float('inf')

def warshall_floyd(graph, V):
    dist = [[graph[i][j] for j in range(V)] for i in range(V)]
    
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][k] + dist[k][j], dist[i][j])
    
    return dist

N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]

G = {}
for i in range(N):
    G[i] = {}
    for j in range(N):
        if i == j:
            G[i][j] = 0
        else:
            G[i][j] = INF

for a, b, t in edges:
    G[a - 1][b - 1] = t
    G[b - 1][a - 1] = t

dist = warshall_floyd(G, N)
ans = 10 ** 10
for row in dist:
    ans = min(ans, max(row))
print(ans)