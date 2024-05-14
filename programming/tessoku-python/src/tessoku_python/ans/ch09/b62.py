import sys

sys.setrecursionlimit(120000)


N, M = map(int, input().split())
edges = [list(map(int, input().split())) for i in range(M)]

G = [list() for i in range(N + 1)]

for a, b in edges:
    G[a].append(b)
    G[b].append(a)

visited = [False] * (N + 1)
path = []

def dfs(i: int):
    path.append(i)
    if i == N:
        for x in path:
            print(x, end=" ")
        print()
        exit(0)
    
    visited[i] = True
    for j in G[i]:
        if not visited[j]:
            dfs(j)
    path.pop()

dfs(1)