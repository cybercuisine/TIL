N = int(input())
H = list(map(int, input().split()))

dp = [0, abs(H[0]-H[1])]

for i in range(2, N):
    route = min(dp[i-1] + abs(H[i] - H[i-1]), dp[i-2] + abs(H[i] - H[i-2]))
    dp.append(route)

print(dp[-1])