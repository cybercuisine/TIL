# Python TLE, PyPy MLE even in correct solution
M, N = map(int, input().split())
K = int(input())
joi = [input() for _ in range(M)]
district = [list(map(int, input().split())) for _ in range(K)]

S = [[[0, 0, 0] for _ in range(N + 1)] for _ in range(M + 1)]

for i in range(M):
    for j in range(N):
        if joi[i][j] == 'J':
            s = 0
        elif joi[i][j] == 'O':
            s = 1
        else:
            s = 2
        
        for k in range(3):
            S[i + 1][j + 1][k] = S[i][j + 1][k] + S[i + 1][j][k] - S[i][j][k]
        S[i + 1][j + 1][s] += 1

for a, b, c, d in district:
    ans = []
    for i in range(3):
        ans.append(S[c][d][i] - S[a - 1][d][i] - S[c][b - 1][i]  + S[a - 1][b - 1][i])
    print(*ans)