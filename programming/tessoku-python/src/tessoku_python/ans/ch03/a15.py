import bisect

N = int(input())
A = list(map(int, input().split()))

B = []
C = sorted(set(A))

for a in A:
    mid = bisect.bisect_right(C, a)
    B.append(str(mid))

print(' '.join(B))