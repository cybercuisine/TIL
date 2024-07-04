import bisect

D = int(input())
N = int(input())
M = int(input())
shops = [0] + [int(input()) for _ in range(N - 1)] + [D]
K = [int(input()) for _ in range(M)]

shops.sort()
ans = 0
for k in K:
    idx = bisect.bisect_left(shops, k)
    cnt = abs(k - shops[idx])
    if idx >= 1:
        cnt = min(abs(k - shops[idx - 1]), cnt)
    ans += cnt

print(ans)