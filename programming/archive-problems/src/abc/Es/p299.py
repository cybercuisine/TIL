from collections import deque

N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    u, v = u - 1, v - 1
    G[u].append(v)
    G[v].append(u)

Q = [[] for _ in range(N + 1)]
dst = [0] * N
L = []
K = int(input())
for _ in range(K):
    p, d = map(int, input().split())
    p -= 1
    L.append([p, d])
    Q[d].append(p)

for i in range(1, N + 1)[::-1]:
    while Q[i]:
        x = Q[i].pop()
        if dst[x] < -i:
            continue
        dst[x] = -i
        for y in G[x]:
            if dst[y] <= dst[x] + 1:
                continue
            dst[y] = dst[x] + 1
            Q[i - 1].append(y)

Q = deque()
C = ["1"] * N
check = [100000] * N
for i in range(N):
    if dst[i]:
        C[i] = "0"
    else:
        Q.append(i)
        check[i] = 0

while Q:
    x = Q.popleft()
    for y in G[x]:
        if check[y] <= check[x] + 1:
            continue
        check[y] = check[x] + 1
        Q.append(y)

for p, d in L:
    if check[p] == d:
        continue
    print("No")
    exit()

print("Yes")
print("".join(C))
