N = int(input())
A = list(map(int, input().split()))

S = [0] * N
T = [-1] * N
for now in range(N):
    if S[now] != 0:
        continue
    R = []
    vis = 0
    while True:
        if S[now] != 0 or T[now] != -1:
            break

        T[now] = vis
        R.append(now)
        now = A[now] - 1
        vis += 1

    loop = len(R) - T[now]
    memo = S[now] != 0
    lastT = T[now]
    for j in range(len(R)):
        r = R[len(R) - 1 - j]
        if memo:
            S[r] = S[now] + j + 1
        else:
            if lastT <= T[r]:
                S[r] = loop
            else:
                S[r] = loop + lastT - T[r]

        T[r] = -1

print(sum(S))
