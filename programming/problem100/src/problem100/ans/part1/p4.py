N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]


ans = 0
for i in range(M):
    for j in range(i + 1, M):
        score = 0
        for k in range(N):
            score += max(A[k][i], A[k][j])
        ans = max(ans, score)

print(ans)