A, B, C, X, Y = map(int, input().split())

if A + B <= 2 * C:
    print(A*X + B*Y)
    exit(0)

ans = 0

ans += 2 * C * min(X, Y)

if X > Y:
    X -= Y
    ans += min(A * X, 2 * C * X)
else:
    Y -= X
    ans += min(B * Y, 2 * C * Y)

print(ans)