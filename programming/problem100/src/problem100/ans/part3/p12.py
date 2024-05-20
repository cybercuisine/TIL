from itertools import product

N, M = map(int, input().split())
relations = [list(map(int, input().split())) for i in range(M)]

G = {}
for i in range(1, N + 1):
    G[i] = []
for x, y in relations:
    G[x].append(y)
    G[y].append(x)

ans = 0

arr = []
for bits in product([0, 1], repeat=N):
    arr.clear()
    for i in range(N):
        if bits[i] == 1:
            arr.append(i + 1)
    
    flg = True
    for i in arr:
        for j in arr:
            if i == j:
                continue
            if j not in G[i]:
                flg = False

    if flg:
        ans = max(ans, len(arr))

print(ans)