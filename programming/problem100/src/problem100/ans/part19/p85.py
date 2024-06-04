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

N, Q = map(int, input().split())
ans = []
uf = UnionFind(N)
for i in range(Q):
    com, x, y = map(int, input().split())
    if com == 0:
        uf.union(x, y)
    else:
        ans.append(1 if uf.connected(x, y) else 0)

print(*ans, sep='\n')