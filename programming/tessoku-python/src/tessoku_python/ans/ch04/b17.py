N = int(input())
h = list(map(int, input().split()))

dp = [0, abs(h[0]-h[1])]

for i in range(2, N):
    route = min(dp[i-1] + abs(h[i] - h[i-1]), dp[i-2] + abs(h[i]- h[i-2]))
    dp.append(route)

routes = []
place = N - 1
while True:
    routes.append(place + 1)
    if place == 0:
        break
    if dp[place-1] + abs(h[place] - h[place-1]) == dp[place]:
        place -= 1
    else:
        place -= 2
    
print(len(routes))
print(" ".join([str(route) for route in reversed(routes)]))