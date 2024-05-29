N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]

G = {}
counts = [0] * (N + 1)
for i in range(N + 1):
    G[i] = []
for x, y in edges:
    G[x].append(y)
    counts[y] += 1


dp = [0] * (N + 1)
queue = [i for i in range(1, N + 1) if counts[i] == 0]

while len(queue):
    i = queue.pop()
    for j in G[i]:
        dp[j] = max(dp[j], dp[i] + 1)
        counts[j] -= 1
        if counts[j] == 0:
            queue.append(j)

print(max(dp))