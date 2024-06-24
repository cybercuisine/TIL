from collections import defaultdict, deque
from typing import Dict, List

def detect_cycle(graph: Dict[int, List[int]]) -> bool:
    visited = set()

    for start_node in graph:
        if start_node in visited:
            continue

        queue = deque([(start_node, None)])
        node_parent = {}

        while queue:
            node, parent = queue.popleft()

            if node in visited:
                return True

            visited.add(node)
            node_parent[node] = parent

            for neighbor in graph[node]:
                if neighbor != parent:
                    if neighbor in visited:
                        return True
                    queue.append((neighbor, node))

    return False

N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]

G = defaultdict(list)
for a, b in AB:
    G[a].append(b)
    G[b].append(a)

for i in range(1, N + 1):
    if len(G[i]) > 2:
        print("No")
        exit()

if detect_cycle(G):
    print("No")
else:
    print("Yes")