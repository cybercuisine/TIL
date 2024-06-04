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
query = [list(map(int, input().split())) for _ in range(M)]


ans = 0
for i in range(M):
    uf = UnionFind(N + 1)
    for j in range(M):
        if i == j:
            continue
        a, b = query[j]
        uf.union(a, b)
    a, b = query[i]
    if not uf.connected(a, b):
        ans += 1

print(ans)
