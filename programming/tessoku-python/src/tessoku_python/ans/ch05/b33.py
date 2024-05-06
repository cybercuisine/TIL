N, H, W = map(int, input().split())
A = [None] * N
B = [None] * N
X = []
for i in range(N):
    A[i], B[i] = map(int, input().split())
    X.append(A[i] - 1)
    X.append(B[i] - 1)


nim = X[0]
for i in range(1, 2*N):
    nim = nim ^ X[i]

if nim != 0:
    print("First")
else:
    print("Second")