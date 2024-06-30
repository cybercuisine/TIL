from sortedcontainers import SortedList

Q = int(input())
query = [list(map(int, input().split())) for _ in range(Q)]

pls = 0
bag = SortedList([])
for q in query:
    if q[0] == 1:
        bag.add(q[1] - pls)
    elif q[0] == 2:
        pls += q[1]
    else:
        f = bag.pop(0)
        print(f + pls)