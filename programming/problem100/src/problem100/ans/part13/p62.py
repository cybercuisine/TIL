
def warshall_floyd(graph, V):
    dist = [[graph[i][j] for j in range(V)] for i in range(V)]
    
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][k] + dist[k][j], dist[i][j])
    
    return dist

H, W = map(int, input().split())
C = [tuple(map(int, input().split())) for i in range(10)]
A = [list(map(int, input().split())) for i in range(H)]


dist = warshall_floyd(C, 10)

cost = 0
for i in range(H):
    for j in range(W):
        if A[i][j] == -1:
            continue
        cost += dist[A[i][j]][1]

print(cost)
