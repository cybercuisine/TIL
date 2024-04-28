H,W,N = map(int, input().split())
A = [None] * (N+1)
B = [None] * (N+1)
C = [None] * (N+1)
D = [None] * (N+1)
for i in range(1, N+1):
    A[i],B[i],C[i],D[i] = map(int, input().split())

ans = [[0]*(W+2) for i in range(H+2)]
X = [[0]*(W+2) for i in range(H+2)]

for i in range(1,N+1):
    X[A[i]][B[i]] += 1
    X[A[i]][D[i]+1] -= 1
    X[C[i]+1][B[i]] -= 1
    X[C[i]+1][D[i]+1] += 1

for i in range(1, H + 1):
    for j in range(1, W + 1):
        ans[i][j] = ans[i][j-1] + X[i][j]

for j in range(1, W + 1):
    for i in range(1, H + 1):
        ans[i][j] += ans[i-1][j]
    
for i in range(1, H + 1):
    for j in range(1, W + 1):
        print(ans[i][j], end=' ')
    print()
