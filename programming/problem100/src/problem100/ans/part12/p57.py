import heapq


N, K = map(int, input().split())

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


G = {}
ans = []
for i in range(N):
    G[i + 1] = {}
    for j in range(N):
        G[i + 1][j + 1] = float('inf')
for _ in range(K):
    edge = list(map(int, input().split()))
    if edge[0] == 1:
        c, d, e = edge[1], edge[2], edge[3]
        G[c][d] = min(G[c][d], e)
        G[d][c] = min(G[d][c], e)
    else:
        a, b = edge[1], edge[2]
        distances, shortest_path = dijkstra(G, a)
        ans.append(distances[b])

for a in ans:
    if a == float('inf'):
        print('-1')
    else:
        print(a)