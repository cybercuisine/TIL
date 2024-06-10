N = int(input())
P = list(map(int, input().split()))
G = [[] for i in range(N)]
for i in range(N - 1):
    G[P[i] - 1].append(i + 1)
A = list(map(int,input().split()))

dp = [10 ** 10] * N
for i in range(N - 1, -1, -1):
    v = [10 ** 10] * 5001
    v[0] = 0
    for j in G[i]:
        v2 = [10 ** 10] * 5001
        x = dp[j]
        for k in range(5000, -1, -1):
            if k + A[j] <= 5000:
              v2[k + A[j]] = min(v2[k + A[j]], v[k] + x)
            if k + x <= 5000:
                v2[k + x] = min(v2[k + x], v[k] + A[j])
        v = v2[:]
    z = min(v[:A[i] + 1])
    if z > 10 ** 8:
        print('IMPOSSIBLE')
        exit()
    dp[i] = z

print('POSSIBLE')