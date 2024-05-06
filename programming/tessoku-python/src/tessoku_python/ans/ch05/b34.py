N, X, Y = map(int, input().split())
A = list(map(int, input().split()))

xor = 0
for i in range(N):
    grundy = [0,0,1,1,2]
    xor ^= grundy[A[i] % 5]

if xor != 0:
    print("First")
else:
    print("Second")