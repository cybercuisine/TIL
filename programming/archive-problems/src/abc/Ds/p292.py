from collections import defaultdict, deque

N, M = map(int, input().split())
UV = [list(map(int, input().split())) for _ in range(M)]

G = defaultdict(list)
for u, v in UV:
    G[u].append(v)
    G[v].append(u)

visited = [False] * (N + 1)

def bfs_component(start):
    queue = deque([start])
    visited[start] = True
    vertices_count = 0
    edges_count = 0

    while queue:
        vertex = queue.popleft()
        vertices_count += 1
        for neighbor in G[vertex]:
            edges_count += 1
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

    edges_count //= 2

    return vertices_count, edges_count

flg = True

for i in range(1, N + 1):
    if not visited[i]:
        v, e = bfs_component(i)
        flg &= (v == e)


print("Yes" if flg else "No")