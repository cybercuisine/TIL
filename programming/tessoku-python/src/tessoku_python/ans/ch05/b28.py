N = int(input())

A = [1, 1]

for i in range(2, N):
    a = (A[i-1] + A[i-2]) % (10** 9 + 7)
    A.append(a)

print(A[-1])