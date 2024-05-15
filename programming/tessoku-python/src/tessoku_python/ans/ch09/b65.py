import sys
sys.setrecursionlimit(1 << 30)

N, T = map(int, input().split())
T -= 1
g = [[] for i in range(N)]

for i in range(N - 1):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    g[A].append(B)
    g[B].append(A)

rank = [0] * N

def dfs(parent: int, i: int) -> int:
    for j in g[i]:
        if j == parent:
            continue
        r = dfs(i, j) + 1
        if rank[i] < r:
            rank[i] = r
    return rank[i]

dfs(-1, T)
print(*rank)