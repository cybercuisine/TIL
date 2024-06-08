N, D = map(int, input().split())

cnt2 = 0
cnt3 = 0
cnt5 = 0

while D % 2 == 0:
    D //= 2
    cnt2 += 1
while D % 3 == 0:
    D //= 3
    cnt3 += 1
while D % 5 == 0:
    D //= 5
    cnt5 += 1

if D != 1:
    print(0)
    exit()

dp = [[[[0] * (cnt5 + 1) for i in range(cnt3 + 1)] for j in range(cnt2 + 1)] for k in range(N + 1)]
dp[0][0][0][0] = 1

d2 = [0, 1, 0, 2, 0, 1]
d3 = [0, 0, 1, 0, 0, 1]
d5 = [0, 0, 0, 0, 1, 0]

for i in range(N):
    for c2 in range(cnt2 + 1):
        for c3 in range(cnt3 + 1):
            for c5 in range(cnt5 + 1):
                for j in range(6):
                    nc2 = min(cnt2, c2 + d2[j])
                    nc3 = min(cnt3, c3 + d3[j])
                    nc5 = min(cnt5, c5 + d5[j])
                    dp[i + 1][nc2][nc3][nc5] += (dp[i][c2][c3][c5] / 6)

print(dp[N][cnt2][cnt3][cnt5])