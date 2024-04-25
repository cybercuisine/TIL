N = int(input())
X = [0] * N
Y = [0] * N
for i in range(N):
    X[i], Y[i] = list(map(int, input().split()))
Q = int(input())
A = [ None ] * Q
B = [ None ] * Q
C = [ None ] * Q
D = [ None ] * Q
for i in range(Q):
	A[i], B[i], C[i], D[i] = map(int, input().split())

mx = 1501

T = [[0 for i in range(mx)] for j in range(mx)]
Z = [[0 for i in range(mx)] for j in range(mx)]

for i in range(N):
    T[X[i]][Y[i]] += 1

for i in range(1, mx):
    for j in range(1, mx):
        Z[i][j] = Z[i-1][j] + T[i][j]

for j in range(1, mx):
    for i in range(1, mx):
        Z[i][j] += Z[i][j-1]

for i in range(Q):
    a = A[i]
    b = B[i]
    c = C[i]
    d = D[i]
    print(Z[c][d] + Z[a-1][b-1] - Z[a-1][d] - Z[c][b-1])