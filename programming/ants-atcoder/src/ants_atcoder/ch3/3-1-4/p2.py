from collections import *
from itertools import *
from functools import *


class Dsu:
    def __init__(self, n):
        self.f = list(range(n))
        self.sz = [1] * n

    def find(self, x):
        xcopy = x
        while x != self.f[x]:
            x = self.f[x]
        while xcopy != x:
            self.f[xcopy], xcopy = x, self.f[xcopy]
        return x

    def same(self, u, v):
        return self.find(u) == self.find(v)

    def merge(self, u, v) -> bool:
        u = self.find(u)
        v = self.find(v)
        if u == v:
            return False
        self.sz[u] += self.sz[v]
        self.f[v] = u
        return True

    def size(self, x):
        return self.sz[self.find(x)]


def LI():
    return list(map(int, input().split()))


def I():
    return int(input())


def solve():
    N, M = LI()
    edges = []
    for _ in range(M):
        a, b, c, t = LI()
        edges.append((a, b, c, t))

    def check(x: float) -> bool:
        dsu = Dsu(N)
        es = []
        for a, b, c, t in edges:
            es.append((a, b, c - x * t))
        es.sort(key=lambda v: v[2])
        cost = 0
        for i in range(M):
            a, b, w = es[i]
            if w <= 0:
                cost += w
                dsu.merge(a, b)
            elif not dsu.same(a, b):
                cost += w
                dsu.merge(a, b)

        return cost <= 0

    L, R = 0.0, 10**14
    for _ in range(100):
        mid = (L + R) / 2
        if check(mid):
            R = mid
        else:
            L = mid
    print("{0:.2f}".format(L))


solve()
