import bisect

d = int(input())
n = int(input())
m = int(input())
shops = [0] + [int(input()) for _ in range(n-1)] + [d]
homes = [int(input()) for _ in range(m)]

shops.sort()

ans = 0

arr = []
for home in homes:
    idx = max(bisect.bisect_left(shops, home), 0)
    arr.clear()
    arr.append(abs(shops[idx] - home))
    if idx + 1 <= n:
        arr.append(abs(shops[idx+1] - home))
    if idx - 1 >= 0:
        arr.append(abs(shops[idx-1] - home))

    ans += min(arr)

print(ans)