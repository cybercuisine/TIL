import bisect

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort()
C.sort()

ans = 0
for b in B:
    idx_a = bisect.bisect_left(A, b)
    idx_c = bisect.bisect_right(C, b)

    ans += idx_a * (N - idx_c)

print(ans)