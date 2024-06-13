import sys


sys.setrecursionlimit(10 ** 6)

N, M = map(int, input().split())
G = [[] for _ in range(N)]

for _ in range(M):
    u, v = map(int, input().split())
    u, v = u - 1, v - 1
    G[u].append(v)
    G[v].append(u)

colors = [-1] * N
done = [False] * N
groups = {}


def dfs(v, color, root):
    colors[v] = color
    done[v] = True
    groups[root][color] += 1
    for to in G[v]:
        if colors[to] == color:
            return False
        if colors[to] == -1 and not dfs(to, color ^ 1, root):
            return False
    return True


for i in range(N):
    if done[i]:
        continue
    groups[i] = [0, 0]
    is_bipartite = dfs(i, 0, i)
    if not is_bipartite:
        print(0)
        exit()

group_in = 0
for num_black, num_white in groups.values():
    group_in += num_black * num_white
group_in -= M

group_out = 0
for num_black, num_white in groups.values():
    v = num_black + num_white
    group_out += v * (N - v)

ans = group_in + group_out // 2
print(ans)
