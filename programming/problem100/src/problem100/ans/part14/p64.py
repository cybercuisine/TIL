def kruskal(Edges, V):
    Edges.sort()

    ans = 0
    uf = UnionFind(V)
    for w, (From, To) in Edges:

        if uf.isSame(From, To):
            continue
        else:
            ans += w
            uf.unite(From, To)
    
    return ans

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1 for i in range(n)]
        self.size = [1]*n
    def root(self, x):
        if self.parents[x] == -1:
            return x
        else:
            self.parents[x] = self.root(self.parents[x])
            return self.parents[x]
    def isSame(self, x, y):
        if self.root(x)==self.root(y):
            return True
        else:
            return False
    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x==y:
            return
        if self.size[x] < self.size[y]:
            x, y = y, x

        self.parents[y] = x
        self.size[x] += self.size[y]

V, E = map(int, input().split())
edges = [list(map(int, input().split())) for i in range(E)]

G = []
for s, t, d in edges:
    G.append((d, (s, t)))
    G.append((d, (t, s)))

min_spanning_tree = kruskal(G, V)
print(min_spanning_tree)