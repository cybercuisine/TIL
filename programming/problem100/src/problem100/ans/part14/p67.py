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

N = int(input())
path_x = []
path_y = []
for i in range(N):
    x, y = map(int, input().split())
    path_x.append((x, i))
    path_y.append((y, i))

path_x.sort()
path_y.sort()

edges = []
for i in range(N - 1):
    edges.append((path_x[i + 1][0] - path_x[i][0], path_x[i][1], path_x[i + 1][1]))
    edges.append((path_y[i + 1][0] - path_y[i][0], path_y[i][1], path_y[i + 1][1]))

edges.sort()

uf = UnionFind(N)
cost = 0
for c, city1, city2 in edges:
    if not uf.same(city1, city2):
        uf.union(city1, city2)
        cost += c

print(cost)