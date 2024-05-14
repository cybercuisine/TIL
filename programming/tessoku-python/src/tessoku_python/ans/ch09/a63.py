from collections import deque

N, M = map(int, input().split())
edges = [list(map(int, input().split())) for i in range(M)]

G = [list() for i in range(N + 1)]

for a, b in edges:
    G[a].append(b)
    G[b].append(a)

dist = [-1] * (N + 1)
dist[1] = 0

Q = deque()
Q.append(1)

while len(Q) >= 1:
    pos = Q.popleft()
    for nex in G[pos]:
        if dist[nex] == -1:
            dist[nex] = dist[pos] + 1
            Q.append(nex)

for i in range(1, N + 1):
    print(dist[i])