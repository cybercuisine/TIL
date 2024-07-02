class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parent_size = [-1] * n

    def merge(self, a, b):
        x, y = self.leader(a), self.leader(b)
        if x == y:
            return
        if abs(self.parent_size[x]) < abs(self.parent_size[y]):
            x, y = y, x
        self.parent_size[x] += self.parent_size[y]
        self.parent_size[y] = x
        return

    def same(self, a, b):
        return self.leader(a) == self.leader(b)

    def leader(self, a):
        if self.parent_size[a] < 0:
            return a
        self.parent_size[a] = self.leader(self.parent_size[a])
        return self.parent_size[a]

    def size(self, a):
        return abs(self.parent_size[self.leader(a)])

    def groups(self):
        result = [[] for _ in range(self.n)]
        for i in range(self.n):
            result[self.leader(i)].append(i)
        return [r for r in result if r != []]


N = int(input())
A = list(map(int, input().split()))

Uni = UnionFind(10**6)

ans = 0

for i in range(N // 2):
    A_left = A[i]
    A_right = A[N - i - 1]
    if Uni.same(A_left, A_right) is False:
        ans += 1
        Uni.merge(A_left, A_right)

print(ans)
