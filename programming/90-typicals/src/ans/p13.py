import heapq


N, M = map(int, input().split())
ABC = [list(map(int, input().split())) for _ in range(M)]


def dijkstra(graph, start):
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))
    distances = {node: float("inf") for node in graph}
    distances[start] = 0
    shortest_path = {node: None for node in graph}

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


G = {}
for i in range(1, N + 1):
    G[i] = {}
for a, b, c in ABC:
    G[a][b] = c
    G[b][a] = c

from_1, _ = dijkstra(G, 1)
from_n, _ = dijkstra(G, N)

for i in range(1, N + 1):
    print(from_1[i] + from_n[i])