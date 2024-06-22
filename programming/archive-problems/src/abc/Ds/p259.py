import math

class UnionFind():
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
        if rx == ry: return False
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.par[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        self.siz[rx] += self.siz[ry]
        return True
    
    def size(self, x):
        return self.siz[self.root(x)]

N = int(input())
sx, sy, tx, ty = map(int, input().split())
XYR = [list(map(int, input().split())) for _ in range(N)]

UF = UnionFind(N)

for i in range(N):
    x1, y1, r1 = XYR[i]
    for j in range(N):
        if i == j:
            continue
        x2, y2, r2 = XYR[j]

        d = (x1 - x2) ** 2 + (y1 - y2) ** 2

        if (r1 - r2) ** 2 <= d <= (r1 + r2) ** 2:
            UF.unite(i, j)

s = -1
t = -1
for i in range(N):
    x1, y1, r1 = XYR[i]
    if (x1 - sx) ** 2 + (y1 - sy) ** 2 == r1 ** 2:
        s = i
    if (x1 - tx) ** 2 + (y1 - ty) ** 2 == r1 ** 2:
        t = i

if s == t or UF.is_same(s, t):
    print("Yes")
else:
    print("No")
