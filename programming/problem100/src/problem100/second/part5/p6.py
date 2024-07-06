import bisect

N, M = map(int, input().split())
P = [int(input()) for _ in range(N)]

P2 = []
for i in range(N):
    P2.append(P[i])
    for j in range(N):
        p = P[i] + P[j]
        P2.append(p)

P2.sort()

ans = 0

idx = bisect.bisect_right(P2, M) - 1
if idx >= 0:
    ans = max(ans, P2[idx])

for p in P2:
    m = M - p
    idx = bisect.bisect_right(P2, m) - 1
    if idx >= 0 and idx < len(P2):
        ans = max(ans, p + P2[idx])

print(ans)
