N, X = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]

ans = float('inf')
prev = 0
for i in range(N):
    a, b = AB[i]
    if X - i > 0:
        ans = min(ans, a + b * (X - i) + prev)
    prev += (a + b)

print(ans)