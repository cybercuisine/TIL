def MI():
    return map(int, input().split())


def preprocess_coordinates(XY):
    max_d1 = -float("inf")
    min_d1 = float("inf")
    max_d2 = -float("inf")
    min_d2 = float("inf")

    for x, y in XY:
        d1 = x + y
        d2 = x - y
        max_d1 = max(max_d1, d1)
        min_d1 = min(min_d1, d1)
        max_d2 = max(max_d2, d2)
        min_d2 = min(min_d2, d2)

    return max_d1, min_d1, max_d2, min_d2


N, Q = MI()
XY = [list(MI()) for i in range(N)]
query = [int(input()) for i in range(Q)]

max_d1, min_d1, max_d2, min_d2 = preprocess_coordinates(XY)

for q in query:
    q -= 1
    x, y = XY[q]
    d1 = x + y
    d2 = x - y
    max_dist = max(
        abs(max_d1 - d1), abs(min_d1 - d1), abs(max_d2 - d2), abs(min_d2 - d2)
    )
    print(max_dist)
