n = int(input())
G = {}
for i in range(n):
    u, k, *v = map(int, input().split())
    G[u] = v

d = [0] * (n + 1)
f = [0] * (n + 1)
visited = [False]  * (n + 1)
time = 0

def dfs(u):
    global time
    time += 1
    d[u] = time
    visited[u] = True
    for v in sorted(G[u]):
        if not visited[v]:
            dfs(v)
    time += 1
    f[u] = time

for u in range(1, n + 1):
    if not visited[u]:
        dfs(u)

for u in range(1, n + 1):
    print(u, d[u], f[u])