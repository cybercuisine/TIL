from collections import defaultdict, deque


def MI():
    return map(int, input().split())


N, M = MI()
UV = [list(MI()) for i in range(M)]
K = int(input())
PD = [list(MI()) for i in range(K)]

G = defaultdict(list)
for u, v in UV:
    G[u].append(v)
    G[v].append(u)


def bfs(start):
    dist = [-1] * (N + 1)
    queue = deque([start])
    dist[start] = 0
    while queue:
        node = queue.popleft()
        for neighbor in G[node]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[node] + 1
                queue.append(neighbor)
    return dist


all_distances = [[]]
for i in range(1, N + 1):
    all_distances.append(bfs(i))

ans = ["1"] * (N + 1)
for pi, di in PD:
    for j in range(1, N + 1):
        if all_distances[pi][j] < di:
            ans[j] = "0"

for pi, di in PD:
    cnt = float("inf")
    for j in range(1, N + 1):
        dist = all_distances[pi][j]
        if ans[j] == "1":
            cnt = min(cnt, dist)
    if cnt != di:
        print("No")
        exit()

print("Yes")
print(*ans[1:], sep="")
