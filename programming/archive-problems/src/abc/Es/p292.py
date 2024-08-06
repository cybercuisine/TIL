from collections import defaultdict


def MI():
    return map(int, input().split())


N, M = MI()
UV = [list(MI()) for i in range(M)]

G = defaultdict(set)
for i in range(1, N + 1):
    G[i] = set()
for u, v in UV:
    G[u].add(v)

cnt = 0
for b in range(1, N + 1):
    for a in range(1, N + 1):
        if a == b or b not in G[a]:
            continue
        for c in G[b]:
            if a != c and c not in G[a]:
                cnt += 1
                G[a].add(c)

print(cnt)