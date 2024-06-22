from collections import defaultdict

N = int(input())
Q = int(input())
queries = [list(map(int, input().split())) for _ in range(Q)]

boxes = defaultdict(list)
cards = defaultdict(set)
for i in range(Q):
    query = queries[i]
    if query[0] == 1:
        i, j = query[1], query[2]
        boxes[j].append(i)
        cards[i].add(j)
    elif query[0] == 2:
        i = query[1]
        print(*sorted(boxes[i]))
    else:
        i = query[1]
        print(*sorted(cards[i]))
