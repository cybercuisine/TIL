import sys

sys.setrecursionlimit(120000)

def dfs(pos, G, visited):
    visited[pos] = True
    for i in G[pos]:
        if visited[i] == False:
            dfs(i, G, visited)

N, M = map(int, input().split())
edges = [list(map(int, input().split())) for i in range(M)]

G = [list() for i in range(N + 1)]

for a, b in edges:
    G[a].append(b)
    G[b].append(a)

visited = [False] * (N + 1)
dfs(1, G, visited)

ans = True
for i in range(1, N + 1):
    if visited[i] == False:
        ans = False

if ans:
    print("The graph is connected.")
else:
    print("The graph is not connected.")