H, W = list(map(int, input().split()))
Z = [ [ 0 ] * (W + 1) for i in range(H + 1) ]
X = [list(map(int, input().split())) for i in range(H)]
Q = int(input())
A = [ None ] * Q
B = [ None ] * Q
C = [ None ] * Q
D = [ None ] * Q
for i in range(Q):
	A[i], B[i], C[i], D[i] = map(int, input().split())
	
for i in range(1, H+1):
	for j in range(1, W+1):
		Z[i][j] = Z[i][j-1] + X[i-1][j-1]
		
for j in range(1, W+1):
	for i in range(1, H+1):
		Z[i][j] += Z[i-1][j]

for i in range(Q):
	print(Z[C[i]][D[i]] + Z[A[i]-1][B[i]-1] - Z[A[i]-1][D[i]] - Z[C[i]][B[i]-1])