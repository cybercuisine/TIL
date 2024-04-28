import sys

N, S = map(int, input().split())
A = list(map(int, input().split()))

dp = [[None]*(S+1) for i in range(N+1)]
dp[0][0] = True
for i in range(1,S+1):
    dp[0][i] = False

for i in range(1, N+1):
    for j in range(0, S+1):
        if j < A[i-1]:
            if dp[i-1][j] == True:
                dp[i][j] = True
            else:
                dp[i][j] = False
        else:
            if dp[i-1][j] == True or dp[i-1][j-A[i-1]] == True:
                dp[i][j] = True
            else:
                dp[i][j] = False

if dp[N][S] == False:
    print(-1)
    sys.exit()

routes = []
card = N
total = S
while True:
    if card == 0:
        break
    if dp[card-1][total] == True:
        total = total
    else:
        routes.append(card)
        total -= A[card-1]
    card -= 1

print(len(routes))
print(" ".join(str(route) for route in reversed(routes)))