from collections import defaultdict
import sys

sys.setrecursionlimit(10 ** 7)

def tarjan_scc(N, G):
    index = 0
    stack = []
    indices = [-1] * (N + 1)
    lowlink = [-1] * (N + 1)
    on_stack = [False] * (N + 1)
    sccs = []

    def strongconnect(v):
        nonlocal index
        indices[v] = lowlink[v] = index
        index += 1
        stack.append(v)
        on_stack[v] = True

        for w in G[v]:
            if indices[w] == -1:
                strongconnect(w)
                lowlink[v] = min(lowlink[v], lowlink[w])
            elif on_stack[w]:
                lowlink[v] = min(lowlink[v], indices[w])

        if lowlink[v] == indices[v]:
            scc = []
            while True:
                w = stack.pop()
                on_stack[w] = False
                scc.append(w)
                if w == v:
                    break
            sccs.append(scc)

    for v in range(1, N + 1):
        if indices[v] == -1:
            strongconnect(v)

    return sccs

N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]

G = defaultdict(list)
for i in range(1, N + 1):
    G[i] = []
for a, b in AB:
    G[a].append(b)

sccs = tarjan_scc(N, G)

def count_pairs(sccs):
    count = 0
    for scc in sccs:
        size = len(scc)
        if size > 1:
            count += size * (size - 1) // 2
    return count

print(count_pairs(sccs))
