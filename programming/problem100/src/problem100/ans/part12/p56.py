import heapq

V, E, r = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(E)]

G = {}
for v in range(V):
    G[v] = {}
for s, t, d in edges:
    G[s][t] = d

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

distances, shortest_path = dijkstra(G, r)
for v in range(V):
    dist = distances[v]
    if dist == float('inf'):
        print('INF')
    else:
        print(dist)