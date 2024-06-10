import bisect

N = int(input())
A = list(map(int, input().split()))

LIS = [A[0]]
for i in range(N):
    if A[i] > LIS[-1]:
        LIS.append(A[i])
    else:
        LIS[bisect.bisect_left(LIS, A[i])] = A[i]

print(len(LIS))