
N, K = map(int, input().split())
A = list(map(int, input().split()))
Q = int(input())
LR = [list(map(int, input().split())) for _ in range(Q)]

cum = [[0] * (N + 1) for _ in range(K)]

for j in range(K):
    for i in range(N):
        cum[j][i + 1] = cum[j][i] + (A[i] if i % K == j else 0)

def get(j, l, r):
    return cum[j][r] - cum[j][l]

results = []

for l, r in LR:
    l -= 1
    same = True
    val = get(0, l, r)
    for j in range(1, K):
        if val != get(j, l, r):
            same = False
            break
    results.append("Yes" if same else "No")

print("\n".join(results))