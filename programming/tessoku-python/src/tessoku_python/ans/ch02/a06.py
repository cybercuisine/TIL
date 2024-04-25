nq = list(map(int, input().split()))
N = nq[0]
Q = nq[1]
A = list(map(int, input().split()))

lrs = [list(map(int, input().split())) for i in range(Q)]

B = []

for i in range(N):
    if i == 0:
        B.append(A[i])
    else:
        B.append(B[i-1] + A[i])

for lr in lrs:
    L = lr[0] - 1
    R = lr[1] - 1
    if L == 0:
        print(B[R])
    else:
        print(B[R]-B[L-1])