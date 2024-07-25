class UnionFind:
    def __init__(self, n):
        self.par = [-1] * n
        self.rank = [0] * n
        self.siz = [1] * n

    def root(self, x):
        if self.par[x] == -1:
            return x
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]

    def is_same(self, x, y):
        return self.root(x) == self.root(y)

    def unite(self, x, y):
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.par[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        self.siz[rx] += self.siz[ry]
        return True

    def size(self, x):
        return self.siz[self.root(x)]


def calc(x, y):
    return x * W + y


H, W = map(int, input().split())
Q = int(input())
query = [list(map(int, input().split())) for i in range(Q)]

grid = [0] * (H * W + 10)

delta = [[0, 1], [1, 0], [0, -1], [-1, 0]]

uf = UnionFind(H * W)

for q in query:
    if q[0] == 1:
        r, c = q[1] - 1, q[2] - 1
        pos = calc(r, c)
        grid[calc(r, c)] = 1
        for dx, dy in delta:
            nr, nc = r + dx, c + dy
            if 0 <= nr < H and 0 <= nc < W:
                pos_n = calc(nr, nc)
                if grid[pos_n] == 1:
                    uf.unite(pos, pos_n)
    elif q[0] == 2:
        ra, ca, rb, cb = q[1] - 1, q[2] - 1, q[3] - 1, q[4] - 1
        A = calc(ra, ca)
        B = calc(rb, cb)
        if grid[A] * grid[B] == 1 and uf.is_same(A, B):
            print("Yes")
        else:
            print("No")