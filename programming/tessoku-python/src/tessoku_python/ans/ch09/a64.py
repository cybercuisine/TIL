import heapq

N, M = map(int, input().split())
edges = [list(map(int, input().split())) for i in range(M)]

G = [list() for i in range(N + 1)]
for a,b,c in edges:
    G[a].append((b,c))
    G[b].append((a,c))

INF = 10 ** 10
kakutei = [False] * (N + 1)
cur = [INF] * (N + 1)
cur[1] = 0
Q = []
heapq.heappush(Q, (cur[1], 1))

while len(Q) >= 1:
    pos = heapq.heappop(Q)[1]

    if kakutei[pos] == True:
        continue

    kakutei[pos] = True
    for e in G[pos]:
        if cur[e[0]] > cur[pos] + e[1]:
            cur[e[0]] = cur[pos] + e[1]
            heapq.heappush(Q, (cur[e[0]], e[0]))

for i in range(1, N + 1):
    if cur[i] != INF:
        print(cur[i])
    else:
        print("-1")