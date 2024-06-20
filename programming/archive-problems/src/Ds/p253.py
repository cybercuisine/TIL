from math import gcd


def sum_multiples(X, N):
    k = N // X
    return X * k * (k + 1) // 2

N, A, B = map(int, input().split())

S = N * (N + 1) // 2

SA = sum_multiples(A, N)
SB = sum_multiples(B, N)

LCM = A * B // gcd(A, B)
SAB = sum_multiples(LCM, N)

result = S - SA - SB + SAB
print(result)
