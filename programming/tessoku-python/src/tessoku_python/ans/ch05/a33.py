N = int(input())
A = list(map(int, input().split()))

nim = A[0]
for i in range(1, N):
    nim = nim ^ A[i]

if nim != 0:
    print("First")
else:
    print("Second")