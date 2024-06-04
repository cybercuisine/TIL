class UnionFind:
    def __init__(self, n) -> None:
        self.parent = list(range(n))
        self.rank = [1] * n
        self.size = [1] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def group_size(self, x):
        return self.size[self.find(x)]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
                self.size[root_x] += self.size[root_y]
            else:
                self.parent[root_x] = root_y
                self.size[root_y] += self.size[root_x]
                if self.rank[root_x] == self.rank[root_y]:
                    self.rank[root_y] += 1
    
    def connected(self, x, y):
        return self.find(x) == self.find(y)
    
N, M = map(int, input().split())
bridges = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(M)]
ans = [0] * (M)
ans[M - 1] = N * (N - 1) // 2

uf = UnionFind(N)
for i in range(M - 2, -1, -1):
    a, b = bridges[i + 1]
    if uf.connected(a, b):
        ans[i] = ans[i + 1]
    else:
        ans[i] = ans[i + 1] - uf.group_size(a) * uf.group_size(b)
    uf.union(a, b)

print(*ans, sep='\n')