A, X, M = map(int, input().split())

if A == 1:
    ans = X % M
else:
    divider = A - 1
    ans = (pow(A, X, M * divider) - 1) // divider % M

print(ans)
