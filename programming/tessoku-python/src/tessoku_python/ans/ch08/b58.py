import bisect

INF = 1 << 61
siz = 1 << 17
dat = [INF] * siz * 2

def update(i: int, v: int) -> None:
    i += siz
    dat[i] = v
    while i > 1:
        i >>= 1
        dat[i] = min(dat[i*2], dat[i*2 + 1])

def query(l: int, r: int) -> int:
    l += siz
    r += siz
    ans = INF
    while l < r:
        if l & 1:
            if ans > dat[l]:
                ans = dat[l]
            l += 1
        if r & 1:
            r -= 1
            if ans > dat[r]:
                ans = dat[r]
        l >>= 1
        r >>= 1
    return ans

N, L, R = map(int, input().split())
X = list(map(int, input().split()))
dp = [0] * N

update(0, 0)

for i in range(1, N):
    x = X[i]
    posL = bisect.bisect_left(X, x - R)
    posR = bisect.bisect_right(X, x - L)
    dp[i] = query(posL, posR) + 1
    update(i, dp[i])

print(dp[-1])