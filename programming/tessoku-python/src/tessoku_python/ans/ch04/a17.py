N = int(input())
A = [0] + list(map(int, input().split()))
B = [0, 0] + list(map(int, input().split()))

dp = [0, A[1]]

for i in range(2, N):
    route = min(dp[i-1] + A[i], dp[i-2] + B[i])
    dp.append(route)

routes = []
place = N - 1
while True:
    routes.append(place + 1)
    if place == 0:
        break
    if dp[place-1] + A[place] == dp[place]:
        place -= 1
    else:
        place -= 2

print(len(routes))
print(" ".join([str(route) for route in reversed(routes)]))