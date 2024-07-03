A, B, C, X, Y = map(int, input().split())

ans = float('inf')

for a in range(X + 1):
    c = 2 * (X - a)
    b = max(0, Y - X + a)
    ans = min(ans, A * a + B * b + C * c)

for b in range(Y + 1):
    c = 2 * (Y - b)
    a = max(0, X - Y + b)
    ans = min(ans, A * a + B * b + C * c)

print(ans)