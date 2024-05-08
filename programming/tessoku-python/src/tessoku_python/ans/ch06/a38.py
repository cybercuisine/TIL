D, N = map(int, input().split())
L = [None] * N
R = [None] * N
H = [None] * N
for i in range(N):
    L[i], R[i], H[i] = map(int, input().split())

lim = [24] * D

for i in range(D):
    for j in range(N):
        if L[j] - 1 <= i and i <= R[j] - 1:
            lim[i] = min(lim[i], H[j])

print(sum(lim))