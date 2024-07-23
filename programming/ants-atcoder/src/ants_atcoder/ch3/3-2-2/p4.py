import bisect
from itertools import accumulate


N = int(input())
A = [int(input()) for _ in range(N)]

S = [0] + list(accumulate(A))
total = S[-1]

left = 0
right = 3 * total
while right - 1 > left:
    mid = (right + left) // 2
    flg = False

    for i in range(1, N + 1):
        idx1 = bisect.bisect_left(S, S[i - 1] + mid)
        if idx1 > N:
            continue
        idx2 = bisect.bisect_left(S, S[idx1] + mid)
        if idx2 > N:
            continue
        if total - S[idx2] + S[i - 1] >= mid:
            flg = True
            break
    
    if flg:
        left = mid
    else:
        right = mid

print(left)
