
class SegTree:
    def __init__(self, data) -> None:
        self.n = len(data)
        self.tree = [0] * 2 * self.n
        self.build(data)

    def build(self, data):
        for i in range(self.n):
            self.tree[self.n + i] = data[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]
    
    def update(self, pos, value):
        pos += self.n
        self.tree[pos] = value
        while pos > 1:
            pos //= 2
            self.tree[pos] = self.tree[pos * 2] + self.tree[pos * 2 + 1]
    
    def query(self, l, r):
        res = 0
        l += self.n
        r += self.n
        while l < r:
            if l % 2:
                res += self.tree[l]
                l += 1
            if r % 2:
                r -= 1
                res += self.tree[r]
            l //= 2
            r //= 2
        return res

N, Q = map(int, input().split())
queries = [list(map(int, input().split())) for i in range(Q)]

A = [0] * N

tree = SegTree(A)

for q in queries:
    tp, *cont = q
    if tp == 1:
        tree.update(cont[0] - 1, cont[1])
    else:
        print(tree.query(cont[0] - 1, cont[1] - 1))