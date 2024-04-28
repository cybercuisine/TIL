N = int(input())
A = [0] + list(map(int, input().split()))

B = [0,0] + list(map(int, input().split()))

dp = [0]

for i in range(1, N):
    route = 0
    if i == 1:
        route = dp[i-1] + A[i]
    else:
        route = min(dp[i-1] + A[i], dp[i-2] + B[i])
    dp.append(route)

print(dp[-1])