# skip
import sys
input = sys.stdin.readline

mod = 10**9 + 7

n = int(input())

g = [[] for i in range(n)]

for _ in range(n - 1):
    a, b = map(lambda x : int(x) - 1, input().split())
    g[a].append(b)
    g[b].append(a)


fa = [-1] * n
sz = [0] * n

def dfs():

    stk = [~0, 0]
    while len(stk):
        u = stk.pop()
        if u >= 0:
            sz[u] = 1
            for j in g[u]:
                if j == fa[u]: continue
                fa[j] = u
                stk.append(~j)
                stk.append(j)
        else:
            u = ~u
            for j in g[u]:
                if j == fa[u]: continue
                sz[u] += sz[j]

dfs()

ans = 0

pow2 = [0] * (n + 1)
pow2[0] = 1
for i in range(1, n + 1):
    pow2[i] = pow2[i - 1] * 2 % mod

for i in range(n):
    p = []
    for j in g[i]:
        if j == fa[i]: p.append(n - sz[i])
        else: p.append(sz[j])
    
    s = pow2[n - 1] - 1
    for x in p:
        s -= pow2[x] - 1
    ans += s

print(ans * pow(pow2[n], mod - 2, mod) % mod)