MOD = 10 ** 5

N, M = map(int, input().split())
D = [0] + [int(input()) for i in range(N - 1)]
A = [int(input()) for _ in range(M)]

arr = [D[0]]
for i in range(1, N):
    arr.append(D[i] + arr[i - 1])

prev = 1
ans = 0
for i in range(M):
    next = prev + A[i]
    if prev == 0:
        ans += arr[next - 1]
    else:
        ans += abs(arr[next - 1] - arr[prev - 1])
    ans %= MOD
    prev = next

print(ans)