N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

ans = 0
j = 0

for i in range(M):
    while B[i] > A[j]:
        j += 1
        if j == N:
            print(-1)
            exit()
    ans += A[j]
    j += 1
    if j == N and i != M - 1:
        print(-1)
        exit()

print(ans)
