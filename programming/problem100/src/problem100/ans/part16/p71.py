MOD = 10 ** 9 + 7

N, Q = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))
C.append(1)

S = [0]
for i in range(1, N):
    S.append((pow(A[i - 1], A[i], MOD) + S[i - 1]) % MOD)

ans = 0
prev = 0
for c in C:
    min_c = min(c - 1, prev)
    max_c = max(c - 1, prev)
    ans += S[max_c] - S[min_c]
    ans %= MOD
    prev = c - 1

print(ans)