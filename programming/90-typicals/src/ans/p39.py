import sys

sys.setrecursionlimit(10**7)


N = int(input())

nodes = [[] for i in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    nodes[a].append(b)
    nodes[b].append(a)


A = [1 for i in range(N)]
flg = [True for i in range(N)]
flg[0] = False


def dfs(v):
    for nv in nodes[v]:
        if not flg[nv]:
            continue
        else:
            flg[nv] = False
            dfs(nv)
            A[v] += A[nv]


dfs(0)
ans = 0
for i in range(N):
    ans += A[i] * (N - A[i])
print(ans)
