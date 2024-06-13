from collections import defaultdict, deque


N, M = map(int, input().split())
R = [list(map(str, input().split())) for _ in range(M)]

X = 0
Y = 0

G = defaultdict(list)

for a, b, c, d in R:
    a, c = int(a), int(c)
    G[a].append(c)
    G[c].append(a)

visited = [False] * (N + 1)

def dfs(node, parent):
    visited[node] = True
    for neighbor in G[node]:
        if not visited[neighbor]:
            if dfs(neighbor, node):
                return True
        elif neighbor != parent:
            return True
    return False

def bfs(start):
    queue = deque([(start, -1)])
    visited[start] = True
    while queue:
        node, parent = queue.popleft()
        for neighbor in G[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append((neighbor, node))
            elif neighbor != parent:
                return True
    return False

for i in range(1, N + 1):
    if not visited[i]:
        if bfs(i):
            X += 1
        else:
            Y += 1

print(X, Y)