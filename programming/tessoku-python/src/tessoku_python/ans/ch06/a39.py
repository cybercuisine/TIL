N = int(input())
A = []
for i in range(N):
    L, R = map(int, input().split())
    A.append([R, L])

A.sort()

current = 0
ans = 0
for i in range(N):
    if current <= A[i][1]:
        current = A[i][0]
        ans += 1

print(ans)