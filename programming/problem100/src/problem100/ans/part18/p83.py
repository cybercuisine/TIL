from itertools import accumulate

N, M = map(int, input().split())
P = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(N - 1)]

S = [0] * N
for m in range(M - 1):
    if P[m] < P[m + 1]:
        S[P[m] - 1] += 1
        S[P[m + 1] - 1] -= 1
    else:
        S[P[m] - 1] -= 1
        S[P[m + 1] - 1] += 1

C = list(accumulate(S))
ans = 0
for n in range(N - 1):
    cnt = C[n]
    ans += min(A[n][0] * cnt, A[n][1] * cnt + A[n][2])

print(ans)