def find_polynomial_B(A, C, N, M):
    B = [0] * (M + 1)
    for i in range(M, -1, -1):
        B[i] = C[N + i] // A[N]
        for j in range(N):
            C[i + j] -= A[j] * B[i]
    return B

N, M = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))
print(*find_polynomial_B(A, C, N, M))