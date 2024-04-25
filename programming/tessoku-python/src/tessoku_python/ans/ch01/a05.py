nk = list(map(int, input().split()))
N = nk[0]
K = nk[1]

ans = 0
for i in range(1, N + 1):
    for j in range(1, N + 1):
        k = K - i - j
        if k >= 1 and k <= N:
            ans += 1

print(ans)