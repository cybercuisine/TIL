class FenwickTree:
    def __init__(self, n):
        self._n = n
        self.data = [0] * n

    def add(self, p, x):
        p += 1
        while p <= self._n:
            self.data[p - 1] += x
            p += p & -p

    def _sum(self, r):
        s = 0
        while 0 < r:
            s += self.data[r - 1]
            r -= r & -r
        return s

    def sum(self, l, r):
        r += 1
        return self._sum(r) - self._sum(l)

    def select(self, p):
        return self.sum(p, p)


N, K = map(int, input().split())
P = list(map(int, input().split()))

FT = FenwickTree(N + 1)

from collections import defaultdict

Deck = defaultdict(list)
DeckNum = 0
CardDeck = [0] * (N + 1)
ans = [-1] * (N + 1)


def Nibutan(x):
    l = x
    r = N
    while 1 < r - l:
        c = (l + r) // 2
        if 1 <= FT.sum(x, c):
            r = c
        else:
            l = c
    return r


for i in range(N):
    X = P[i]
    if K == 1:
        ans[X] = i + 1
    elif FT.sum(X, N) == 0:
        DeckNum += 1
        Deck[DeckNum].append(X)
        FT.add(X, 1)
        CardDeck[X] = DeckNum
    else:
        p = Nibutan(X)
        pNum = CardDeck[p]
        Deck[pNum].append(X)
        FT.add(p, -1)
        FT.add(X, 1)
        CardDeck[X] = pNum
        if len(Deck[pNum]) == K:
            for q in Deck[pNum]:
                ans[q] = i + 1
            FT.add(X, -1)

for i in range(1, N + 1):
    print(ans[i])
