import bisect


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort()
C.sort()

ans = 0
for b in B:
    a_idx = bisect.bisect_left(A, b)
    c_idx = bisect.bisect_right(C, b)

    ans += a_idx * (N - c_idx)

print(ans)