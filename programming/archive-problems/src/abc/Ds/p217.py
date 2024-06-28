from sortedcontainers import SortedList

L, Q = map(int, input().split())
query = [list(map(int, input().split())) for _ in range(Q)]

S = SortedList([0, L])
for c, x in query:
    if c == 1:
        S.add(x)
    else:
        idx = S.bisect_left(x)
        print(S[idx] - S[idx - 1])