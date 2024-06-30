class UnionFind:
    from typing import List

    def __init__(self, n):
        self.n = n
        self.parent = [-1] * n

    def unite(self, x, y) -> int:
        """
        xとyを併合
        """
        x = self.root(x)
        y = self.root(y)

        if x == y:
            return 0

        if self.parent[x] > self.parent[y]:
            x, y = y, x

        self.parent[x] += self.parent[y]
        self.parent[y] = x

        return self.parent[x]

    def is_same(self, x, y) -> bool:
        return self.root(x) == self.root(y)

    def root(self, x) -> int:
        if self.parent[x] < 0:
            return x
        else:
            self.parent[x] = self.root(self.parent[x])
            return self.parent[x]

    def size(self, x) -> int:
        return -self.parent[self.root(x)]

    def all_sizes(self) -> List[int]:
        sizes = []

        for i in range(self.n):
            size = self.parent[i]
            if size < 0:
                sizes.append(-size)
        return sizes

    def groups(self) -> List[List[int]]:
        groups = dict()

        for i in range(self.n):
            p = self.root(i)
            if not groups.get(p):
                groups[p] = []
            groups[p].append(i)

        return list(groups.values())


N = int(input())
G = []

for _ in range(N - 1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    G.append((w, u, v))

G.sort()

ans = 0
uf = UnionFind(N)

for i in range(N - 1):
    w, u, v = G[i]
    x = uf.size(u)
    y = uf.size(v)
    ans += x * y * w
    uf.unite(u, v)
print(ans)


