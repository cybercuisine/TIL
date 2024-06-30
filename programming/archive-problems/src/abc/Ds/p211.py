import math
from heapq import heappush, heappop


def count_shortest_paths(N, edges):
    graph = [[] for _ in range(N + 1)]
    for u, v in edges:
        graph[u].append((v, 1))
        graph[v].append((u, 1))

    shortest_distance = [math.inf] * (N + 1)
    path_count = [0] * (N + 1)

    shortest_distance[1] = 0
    path_count[1] = 1

    minHeap = [(0, 1)]

    while minHeap:
        dist, current_node = heappop(minHeap)

        if dist > shortest_distance[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            if shortest_distance[neighbor] > dist + weight:
                shortest_distance[neighbor] = dist + weight
                path_count[neighbor] = path_count[current_node]
                heappush(minHeap, (dist + weight, neighbor))
            elif shortest_distance[neighbor] == dist + weight:
                path_count[neighbor] = (
                    path_count[neighbor] + path_count[current_node]
                ) % MOD

    return path_count[N]


MOD = 10**9 + 7


N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]

result = count_shortest_paths(N, edges)
print(result)
