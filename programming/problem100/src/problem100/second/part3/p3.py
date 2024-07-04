from collections import defaultdict
from itertools import product


N, M = map(int, input().split())
XY = [list(map(int, input().split())) for _ in range(M)]

G = defaultdict(set)
for x, y in XY:
    G[x].add(y)
    G[y].add(x)

ans = 0
for bits in product([0, 1], repeat=N):
    cnt = sum(bits)
    flg = True

    F = []
    for i in range(N):
        if bits[i] == 1:
            F.append(i + 1)

    for f in F:
        for ff in F:
            if f == ff:
                continue
            if ff not in G[f]:
                flg = False

    if flg:
        ans = max(ans, cnt)

print(ans)