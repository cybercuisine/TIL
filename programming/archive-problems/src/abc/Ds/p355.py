N = int(input())
L = [0] * N
R = [0] * N
for i in range(N):
    L[i], R[i] = map(int, input().split())

L.sort()
R.sort()

ans = N * (N - 1) // 2

j = 0
for i in range(N):
    while R[j] < L[i]:
        j += 1
    ans -= j
print(ans)