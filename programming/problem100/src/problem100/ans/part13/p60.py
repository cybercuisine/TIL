INF = float('inf')

def warshall_floyd(graph, V):
    dist = [[graph[i][j] for j in range(V)] for i in range(V)]
    
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][k] + dist[k][j], dist[i][j])
    
    return dist


V, E = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(E)]
G = {}

for i in range(V):
    G[i] = {}
    for j in range(V):
        if i == j:
            G[i][j] = 0
        else:
            G[i][j] = INF
for s, t, d in edges:
    G[s][t] = d


dist = warshall_floyd(G, V)

outputs = []
for i in range(V):
    out = []
    for j in range(V):
        if i == j and dist[i][j] < 0:
            print('NEGATIVE CYCLE')
            exit()
        out.append(dist[i][j] if dist[i][j] != INF else 'INF')
    outputs.append(out)

for o in outputs:
    print(*o)