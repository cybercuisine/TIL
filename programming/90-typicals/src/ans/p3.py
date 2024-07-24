from collections import deque


N = int(input())
AB = [list(map(int, input().split())) for _ in range(N - 1)]

G = [[] for i in range(N + 1)]
for a, b in AB:
    G[a].append(b)
    G[b].append(a)

def bfs(start):
    dist = [-1] * (N + 1)
    dist[start] = 0
    q = deque([start])
    farthest_node = start
    max_dist = 0
    
    while q:
        node = q.popleft()
        for neighbor in G[node]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[node] + 1
                q.append(neighbor)
                if dist[neighbor] > max_dist:
                    max_dist = dist[neighbor]
                    farthest_node = neighbor
    
    return farthest_node, max_dist

node, _ = bfs(1)

_, diameter = bfs(node)
print(diameter + 1)