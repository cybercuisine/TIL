class UnionFind:
    def __init__(self, n) -> None:
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1
    
    def connected(self, x, y):
        return self.find(x) == self.find(y)

N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]
Q = int(input())
queries = [tuple(map(int, input().split())) for _ in range(Q)]

uf = UnionFind(N)

last = [True] * M
for query in queries:
    if query[0] == 1:
        last[query[1] - 1] = False

for i in range(M):
    a, b = edges[i]
    if last[i]:
        uf.union(a - 1, b - 1)

ans = []
for query in reversed(queries):
    if query[0] == 1:
        edge = edges[query[1] - 1]
        uf.union(edge[0] - 1, edge[1] - 1)
    else:
        u, v = query[1], query[2]
        ans.append("Yes" if uf.connected(u - 1, v - 1) else "No")

for a in reversed(ans):
    print(a)