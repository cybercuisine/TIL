N = int(input())
A = list(map(int, input().split()))
D = int(input())
lrs = [list(map(int, input().split())) for _ in range(D)]

l_max = [0] * N
r_max = [0] * N

l_max[0] = A[0]
for i in range(1, N):
    l_max[i] = max(A[i-1], l_max[i-1])

r_max[N-1] = A[N-1]
for i in reversed(range(0,N-1)):
    r_max[i] = max(A[i], r_max[i+1])

for d in range(D):
    L = lrs[d][0]
    R = lrs[d][1]
    print(max(l_max[L-1], r_max[R]))