import sys

sys.setrecursionlimit(5000)


class SegTree:
    def __init__(self, n):
        self.size = 1
        while self.size < n:
            self.size *= 2
        self.dat = [0] *(self.size * 2)
    
    def update(self, pos, x):
        pos += self.size
        self.dat[pos] = x
        while pos >= 2:
            pos //= 2
            self.dat[pos] = max(self.dat[pos * 2], self.dat[pos * 2 + 1])

    def query(self, l, r, a, b, u):
        if r <= a or b <= l:
            return -1000000000
        if l <= a and b <= r:
            return self.dat[u]
        m = (a + b) // 2
        ans1 = self.query(l, r, a, m, u*2)
        ans2 = self.query(l, r, m, b, u*2 + 1)
        return max(ans1, ans2)
    
N, Q = map(int, input().split())
queries = [list(map(int, input().split())) for i in range(Q)]

Z = SegTree(N)
for q in queries:
    tp, *cont = q
    if tp == 1:
        pos, x = cont
        Z.update(pos - 1, x)
    else:
        l, r = cont
        ans = Z.query(l - 1, r - 1, 0, Z.size, 1)
        print(ans)