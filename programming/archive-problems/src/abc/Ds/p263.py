N, L, R = map(int, input().split())
A = list(map(int, input().split()))


ans = R * N
suma = 0
sumb= 0
maxb = 0

for r in range(N):
    suma += A[r]
    sumb += A[r] - L
    maxb = max(maxb, sumb)
    now = suma + R * (N - r - 1) - maxb
    ans = min(ans, now)

print(ans)