from heapq import heappush, heappop

N, M = map(int, input().split())
edges = [list(map(int, input().split())) for i in range(M)]

G = [list() for i in range(N + 1)]
for a,b,c in edges:
    G[a-1].append((b-1,c))
    G[b-1].append((a-1,c))

INF = 10 ** 10
cost = [INF] * N
back = [-1] * N
q = []

def push(prev: int, i: int, c:int):
    if cost[i] <= c:
        return
    cost[i] = c
    back[i] = prev
    heappush(q, (c, i))

push(-1, N - 1, 0)

while q:
    c, x = heappop(q)
    if cost[x] != c:
        continue
    for j, d in G[x]:
        push(x, j, c + d)

ans = [0]
while ans[-1] != N - 1:
    ans.append(back[ans[-1]])

for x in ans:
    print(x + 1, end=" ")
print()