N, x = map(int, input().split())
A = list(map(int, input().split()))

ans = max(0, A[0] - x)
A[0] = min(A[0], x)
for i in range(1, N):
    cnt = max(0, A[i] + A[i - 1] - x)
    A[i] -= cnt
    ans += cnt

print(ans)