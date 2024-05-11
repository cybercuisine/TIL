import math

def combination(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

N = int(input())
A = list(map(int, input().split()))

X = [0] * 1000000

for i in range(N):
    X[A[i]] += 1


ans = 0
for i in range(N):
    if X[i] >= 3:
        ans += combination(X[i], 3)

print(ans)