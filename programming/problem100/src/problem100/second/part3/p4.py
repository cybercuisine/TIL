from itertools import product

R, C = map(int, input().split())
cookies = [list(map(int, input().split())) for _ in range(R)]

ans = 0

for bits in product([0, 1], repeat=R):
    for i in range(R):
        if bits[i] == 1:
            for j in range(C):
                cookies[i][j] = 1 - cookies[i][j]
    
    cnt = 0
    for j in range(C):
        S = 0
        for i in range(R):
            S += cookies[i][j]
        cnt += max(S, R - S)
    
    ans = max(ans, cnt)
    
    for i in range(R):
        if bits[i] == 1:
            for j in range(C):
                cookies[i][j] = 1 - cookies[i][j]

print(ans)
