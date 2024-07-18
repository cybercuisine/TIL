H, W = map(int, input().split())
A = [[] for _ in range(4)]
low = 10**9
high = 1
for _ in range(H):
    row = list(map(int, input().split()))
    low = min(low, min(row))
    high = max(high, max(row))
    A[0].append(row)

A[1] = [[row[i] for row in A[0][::-1]] for i in range(W)]
A[2] = [row[::-1] for row in A[0][::-1]]
A[3] = [row[::-1] for row in A[1][::-1]]
ans = high - low
for a in A:
    w = len(a[0])
    dp = [0] * (w + 1)
    for row in a:
        left_max = [low]
        for elv in row:
            e = max(left_max[-1], elv)
            left_max.append(e)

        right_min = [high]
        for elv in row[::-1]:
            e = min(right_min[0], elv)
            right_min.insert(0, e)

        dmin = dp[0]
        for i in range(w + 1):
            dmin = min(dmin, dp[i])
            d1 = left_max[i] - low
            d2 = high - right_min[i]
            dp[i] = max(dmin, d1, d2)
    ans = min(ans, min(dp))
print(ans)
