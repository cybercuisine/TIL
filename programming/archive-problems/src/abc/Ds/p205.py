import bisect

N, Q = map(int, input().split())
A = list(map(int, input().split()))
queries = [int(input()) for _ in range(Q)]

largest = 10 ** 19

for k in queries:
    left = 0
    right = largest
    while left < right:
        mid = (left + right) // 2
        idx = bisect.bisect_right(A, mid)
        if k + idx > mid:
            left = mid + 1
        else:
            right = mid
    print(left)
