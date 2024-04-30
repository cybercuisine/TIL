def prev_mass(mass, way):
    if mass == ".":
        return way
    else:
        return 0

H, W = map(int, input().split())
C = [input() for _ in range(H)]

dp = [[0] * W for _ in range(H)]
dp[0][0] = 1

for i in range(H):
    for j in range(W):
        if i > 0 and j > 0:
            dp[i][j] = prev_mass(C[i][j], dp[i-1][j]) + prev_mass(C[i][j], dp[i][j-1])
        elif i > 0:
            dp[i][j] = prev_mass(C[i][j], dp[i-1][j])
        elif j > 0:
            dp[i][j] = prev_mass(C[i][j], dp[i][j-1])

print(dp[H-1][W-1])