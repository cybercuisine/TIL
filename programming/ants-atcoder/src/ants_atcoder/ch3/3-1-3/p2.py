import bisect
from itertools import accumulate

def max_min_piece(N, A):
    A_cum = [0] + list(accumulate(A))
    total_sum = A_cum[-1]

    left = 0
    right = total_sum // 3

    while right - left > 1:
        mid = (left + right) // 2
        valid = False

        for i in range(1, N + 1):
            idx1 = bisect.bisect_left(A_cum, A_cum[i - 1] + mid)
            if idx1 > N:
                continue
            idx2 = bisect.bisect_left(A_cum, A_cum[idx1] + mid)
            if idx2 > N:
                continue
            if total_sum - A_cum[idx2] + A_cum[i - 1] >= mid:
                valid = True
                break

        if valid:
            left = mid
        else:
            right = mid

    return left

N = int(input())
A = [int(input()) for _ in range(N)]

print(max_min_piece(N, A))
