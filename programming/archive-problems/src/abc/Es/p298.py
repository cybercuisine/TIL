MOD = 998244353
N, A, B, P, Q = map(int, input().split())

inv_P = pow(P, MOD - 2, MOD)
inv_Q = pow(Q, MOD - 2, MOD)

dp_T = [[0] * (N + 1) for _ in range(N)]
dp_T[0][A] = 1

dp_A = [[0] * (N + 1) for _ in range(N)]
dp_A[0][B] = 1

for i in range(N - 1):
    for j in range(1, N):
        if dp_T[i][j] > 0:
            for p in range(1, P + 1):
                next_pos = min(N, j + p)
                dp_T[i + 1][next_pos] += dp_T[i][j] * inv_P % MOD
                dp_T[i + 1][next_pos] %= MOD

for i in range(N - 1):
    for j in range(1, N):
        if dp_A[i][j] > 0:
            for q in range(1, Q + 1):
                next_pos = min(N, j + q)
                dp_A[i + 1][next_pos] += dp_A[i][j] * inv_Q % MOD
                dp_A[i + 1][next_pos] %= MOD

prob_T_win = 0

for t in range(N):
    for a in range(N):
        if t <= a:
            prob_T_win += dp_T[t][N] * dp_A[a][N] % MOD
            prob_T_win %= MOD

print(prob_T_win)
