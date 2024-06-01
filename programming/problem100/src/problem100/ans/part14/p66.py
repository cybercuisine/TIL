from collections import defaultdict
import math

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())


ans = []

while True:
    N = int(input())
    if N == 0:
        break
    cells = [list(map(float, input().split())) for _ in range(N)]
    uf = UnionFind(N)
    G = []
    for i in range(N):
        for j in range(i + 1, N):
            ix, iy, iz, ri = cells[i]
            jx, jy, jz, rj = cells[j]
            dist = (ix - jx)**2 + (iy - jy)**2 + (iz - jz)**2
            surface_dist = math.sqrt(dist) - (ri + rj)
            if surface_dist <= 0:
                uf.union(i, j)
            else:
                G.append((surface_dist, i, j))
    G.sort()
    cnt = 0.000
    for cost, u, v in G:
        if not uf.same(u, v):
            cnt += cost
            uf.union(u, v)
    ans.append(cnt)


for a in ans:
    print(f"{a:.3f}")