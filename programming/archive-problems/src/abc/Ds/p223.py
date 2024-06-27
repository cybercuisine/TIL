import heapq


N, M = map(int, input().split())

in_degree = [0] * (N + 1)
adj_list = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().split())
    adj_list[A].append(B)
    in_degree[B] += 1

priority_queue = []

for i in range(1, N + 1):
    if in_degree[i] == 0:
        priority_queue.append(i)

heapq.heapify(priority_queue)

topological_order = []

while priority_queue:
    current = heapq.heappop(priority_queue)
    topological_order.append(current)

    for neighbor in adj_list[current]:
        in_degree[neighbor] -= 1
        if in_degree[neighbor] == 0:
            heapq.heappush(priority_queue, neighbor)

if len(topological_order) == N:
    print(*topological_order)
else:
    print(-1)
