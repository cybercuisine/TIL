H, W, K, V = map(int, input().split())
A = [list(map(int, input().split())) for i in range(H)]

S = [[0] * (W + 1) for _ in range(H + 1)]

for i in range(H):
    for j in range(W):
        S[i + 1][j + 1] = S[i + 1][j] + S[i][j + 1] - S[i][j] + A[i][j]

ans = 0
for i in range(1, H + 1):
    for j in range(1, W + 1):
        for k in range(i, H + 1):
            left = 0
            right = W + 1
            while left < right:
                l = (left + right) // 2
                s = S[k][l] - S[i - 1][l] - S[k][j - 1] + S[i - 1][j - 1] + K * (k - i + 1) * (l - j + 1)
                if s > V:
                    right = l
                else:
                    left = l + 1
            if left < j:
                continue
            if s <= V:
                ans = max(ans, (k - i + 1) * (l - j + 1))

print(ans)