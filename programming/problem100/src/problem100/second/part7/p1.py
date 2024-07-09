from collections import defaultdict, deque


N = int(input())
G = defaultdict(list)
for i in range(N):
    u, k, *v = map(int, input().split())
    G[u] = v

dist = [float("inf")] * (N + 1)
dist[1] = 0
queue = deque([[1, 0]])


while queue:
    cur, length = queue.pop()
    length += 1
    for node in G[cur]:
        if dist[node] > length:
            dist[node] = length
            queue.append([node, length])

for i in range(1, N + 1):
    if dist[i] == float("inf"):
        dist[i] = -1
    print(i, dist[i])
