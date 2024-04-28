N,K = map(int, input().split())
A = list(map(int, input().split()))
R = [0] * N
total = [0] * (N+1)
total[0] = A[0]

for i in range(1, N):
    total[i] = total[i-1] + A[i]

for i in range(N):
    t = 0
    if i==0:
        R[i] = 0
        t = total[R[i]]
    else:
        R[i] = R[i-1]
        t = total[R[i]] - total[i-1]

    while R[i] < N and t <= K:
        R[i] += 1
        t = total[R[i]]
        if i > 0:
            t -= total[i-1]


ans = 0
for i in range(N):
    ans += R[i] - i

print(ans)