N, L = map(int, input().split())
A = [0] * N
B = [0] * N

for i in range(N):
    A[i], B[i] = map(str, input().split())
    A[i] = int(A[i])

ans = 0
for i in range(N):
    if B[i] == "W":
        ans = max(ans, A[i])
    else:
        ans = max(ans, L - A[i])
    
print(ans)