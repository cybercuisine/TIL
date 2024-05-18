import heapq


N, M = map(int, input().split())
paths = [list(map(int, input().split())) for i in range(M)]

weight = 10000
G = [[] for i in range(N + 1)]
for a,b,c,d in paths:
    G[a].append(tuple((b, c * weight - d)))
    G[b].append(tuple((a, c * weight - d)))

INF = 10 ** 10
queue = []
visited = [False] * (N + 1)
cur = [INF] * (N + 1)
cur[1] = 0
heapq.heappush(queue, (cur[1], 1))
while len(queue) > 0:
    pos = heapq.heappop(queue)[1]
    if visited[pos] == True:
        continue
    visited[pos] = True
    for e in G[pos]:
        if cur[e[0]] > cur[pos] + e[1]:
            cur[e[0]] = cur[pos] + e[1]
            heapq.heappush(queue, (cur[e[0]], e[0]))

dist = (cur[N] + weight - 1) // weight
num_trees = dist * 10000 - cur[N]
print(dist, num_trees)