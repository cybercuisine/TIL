def solve():
    ans = []
    INF = 10**10
    while(1):
        N, M = map(int,input().split())
        if N == 0:
            break
        C = [int(input()) for _ in range(M)]
        X = [int(input()) for _ in range(N)]
        dp1 = [INF]*256
        dp2 = [INF]*256
        dp1[128] = 0
        decoder = tuple(tuple(255 if i + c > 255 else 0 if i + c < 0 else i + c for c in C) for i in range(256))
        ls_square = tuple(tuple((x - t)**2 for x in range(256)) for t in range(256))
        for n in range(N):
            x = X[n]
            square = ls_square[x]
            for k in range(256):
                dpnk = dp1[k]
                for code in decoder[k]:
                    # #dp[n+1][d] = min(dp[n+1][d], dp[n][k] + (d-X[n])**2)
                    new = dpnk + square[code]
                    if new < dp2[code]:
                        dp2[code] = new  
            dp1 = dp2[:]
            dp2 = [INF]*256                      
        ans.append(min(dp1))
    for a in ans:
        print(a)
solve()