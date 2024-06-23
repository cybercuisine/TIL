from sortedcontainers import SortedList

A = SortedList([])
Q = int(input())
query = [list(map(int, input().split())) for _ in range(Q)]

for q in query:
    if q[0] == 1:
        A.add(q[1])
    elif q[0] == 2:
        x, k = q[1], q[2]
        idx = A.bisect_right(x)
        if idx - k >= 0:
            print(A[idx - k])
        else:
            print(-1)
    else:
        x, k = q[1], q[2]
        idx = A.bisect_left(x)
        if len(A) >= idx + k:
            print(A[idx + k - 1])
        else:
            print(-1)