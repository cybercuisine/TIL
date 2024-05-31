import heapq
from collections import deque
import bisect

INF = 10 ** 10

def dijkstra(graph, start):
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))
    distances = { node: float('inf') for node in graph }
    distances[start] = 0
    shortest_path = { node: None for node in graph }

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                shortest_path[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, shortest_path

def bfs(graph, C):
    distance = { node: INF for node in graph }
    queue = deque()
    for node in C:
        distance[node] = 0
        queue.append(node)
    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if distance[neighbor] == INF:
                distance[neighbor] = distance[current] + 1
                queue.append(neighbor)
    return distance

def includes(array, num):
    pos = max(bisect.bisect_right(array, num) - 1, 0)
    return array[pos] == num


N, M, K, S = map(int, input().split())
P, Q = map(int, input().split())
C = [int(input()) for _ in range(K)]
AB = [list(map(int, input().split())) for _ in range(M)]

C.sort()

edges = {}
G = {}
for i in range(N):
    edges[i + 1] = []
    G[i + 1] = {}
for a, b in AB:
    edges[a].append(b)
    edges[b].append(a)

dist = bfs(edges, C)

for a, b in AB:
    if includes(C, a) or includes(C, b):
        continue

    if b == N:
        G[a][b] = 0
    elif dist[b] <= S:
        G[a][b] = Q
    else:
        G[a][b] = P
    
    if a == N:
        G[b][a] = 0
    elif dist[a] <= S:
        G[b][a] = Q
    else:
        G[b][a] = P

distances, _ = dijkstra(G, 1)
print(distances[N])