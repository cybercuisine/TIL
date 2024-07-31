from collections import defaultdict
import sys

sys.setrecursionlimit(10 ** 6)

def find_cycles(N, A):
    G = defaultdict(int)
    for i in range(1, N + 1):
        G[i] = A[i - 1]

    visited = [False] * (N + 1)
    in_stack = [False] * (N + 1)
    cycles = []

    def dfs(v):
        stack = []
        while True:
            if not visited[v]:
                visited[v] = True
                in_stack[v] = True
                stack.append(v)
                v = G[v]
            elif in_stack[v]:
                cycle_start_index = stack.index(v)
                cycles.append(stack[cycle_start_index:])
                break
            else:
                break
        for node in stack:
            in_stack[node] = False

    for i in range(1, N + 1):
        if not visited[i]:
            dfs(i)

    flat_cycles = [node for cycle in cycles for node in cycle]
    return set(flat_cycles)

N = int(input())
A = list(map(int, input().split()))

G = defaultdict(int)
for i in range(1, N + 1):
    G[i] = A[i - 1]

cycles = find_cycles(N, A)
ans = 0
for i in range(1, N + 1):
    if i in cycles:
        ans += 1

print(ans)
