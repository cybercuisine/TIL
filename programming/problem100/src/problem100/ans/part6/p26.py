import sys
sys.setrecursionlimit(10 ** 7)

N, Q = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(N - 1)]
queries = [tuple(map(int, input().split())) for _ in range(Q)]

counters = [0] * (N + 1)
G = {}
for i in range(1, N + 1):
    counters[i] = 0
    G[i] = []

for a, b in edges:
    G[a].append(b)
    G[b].append(a)

for p, x in queries:
    counters[p] += x

def dfs(i, prev = -1):
    for next in G[i]:
        if next == prev:
            continue
        counters[next] += counters[i]
        dfs(next, i)

dfs(1)
print(*counters[1:])