N, K = map(int, input().split())
A = [0] * N
B = [0] * N

for i in range(N):
    A[i], B[i] = map(int, input().split())

ans = 0
for a in range(1, 101):
    for b in range(1, 101):
        attends = 0
        for k in range(N):
            if a <= A[k] <= a + K and b <= B[k] <= b + K:
                attends += 1
        ans = max(ans, attends)

print(ans)