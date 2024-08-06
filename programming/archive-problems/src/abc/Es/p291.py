from collections import deque, defaultdict


def MI():
    return map(int, input().split())


def topological_sort(N, edges):
    in_degree = [0] * N
    graph = defaultdict(list)

    for x, y in edges:
        graph[x].append(y)
        in_degree[y] += 1

    queue = deque([i for i in range(N) if in_degree[i] == 0])
    sorted_list = []

    while queue:
        if len(queue) > 1:
            return None
        node = queue.popleft()
        sorted_list.append(node)

        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(sorted_list) == N:
        return sorted_list
    else:
        return None


N, M = MI()
XY = [tuple(map(lambda x: int(x) - 1, MI())) for _ in range(M)]

sorted_list = topological_sort(N, XY)

if sorted_list is None:
    print("No")
else:
    A = [0] * N
    for i, val in enumerate(sorted_list):
        A[val] = i + 1
    print("Yes")
    print(*A)
