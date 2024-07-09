from collections import defaultdict
import sys

sys.setrecursionlimit(10 ** 6)

N, Q = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N - 1)]
PX = [list(map(int, input().split())) for _ in range(Q)]

G = defaultdict(list)
for a, b in AB:
    G[a].append(b)
    G[b].append(a)

visited = [False] * (N + 1)
counters = [0] * (N + 1)

for p, x in PX:
    counters[p] += x

def dfs(p, cnt):
    counters[p] += cnt
    visited[p] = True

    for node in G[p]:
        if not visited[node]:
            dfs(node, counters[p])

dfs(1, 0)
for i in range(1, N + 1):
    print(counters[i], end=' ')

print()