import bisect

N, M = map(int, input().split())
P = [0] + [int(input()) for _ in range(N)]

# P.sort()
score = 0

P1 = set([])
for p in P:
    for q in P:
        if p + q <= M:
            P1.add(p + q)
P1 = list(P1)
P1.sort()

for p in P1:
    idx = bisect.bisect_right(P1, M - p) - 1
    if idx >= 0 and p + P1[idx] <= M:
        score = max(score, p + P1[idx])

print(score)