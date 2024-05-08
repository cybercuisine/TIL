N, D = map(int, input().split())
X = [None] * N
Y = [None] * N
for i in range(N):
    X[i], Y[i] = map(int, input().split())

used = [False] * N

ans = 0
for i in range(1, D+1):
    max_value = 0
    maxID = -1
    for j in range(N):
        if used[j] == False and max_value < Y[j] and X[j] <= i:
            max_value = Y[j]
            maxID = j
    
    if maxID != -1:
        ans += max_value
        used[maxID] = True

print(ans)
