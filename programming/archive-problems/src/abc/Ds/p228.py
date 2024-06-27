import bisect
from sortedcontainers import SortedList

Q = int(input())
TX = [list(map(int, input().split())) for _ in range(Q)]

N = 2 ** 20

F = [i for i in range(N)]
F = SortedList(F)

A = [-1] * N

for t, x in TX:
    if t == 1:
        idx = bisect.bisect_left(F, x % N)
        if idx == len(F):
            idx = 0
        A[F[idx]] = x
        F.remove(F[idx])
    else:
        print(A[x % N])