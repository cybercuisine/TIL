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

def kruskal(edges: list, num_of_vertices: int):
    uf = UnionFind(num_of_vertices)
    total = 0
    edges.sort(key=lambda x: x[2], reverse=True)

    for u, v, cost in edges:
        u -= 1
        v -= 1
        if not uf.connected(u, v):
            uf.union(u, v)
            total += cost

    return total

N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]

print(kruskal(edges, N))